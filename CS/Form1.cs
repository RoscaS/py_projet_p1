using InTheHand.Net;
using InTheHand.Net.Bluetooth;
using InTheHand.Net.Sockets;
using InTheHand.Windows.Forms;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows.Forms;

namespace drawing_robot_simulator
{
    public partial class Form1 : Form
    {
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        public const int ZOOMFACTOR = 3;

        public RobotArm Arm_1, Arm_2;
        public PointF i1, i2, ARMPointA;
        public PointF SheetCoord;
        public List<PixelPointF> DrawPointList = new List<PixelPointF>();
            // trouver fichier pixelpointF. 
            // stylo up/down --> isPenEngaged (coords var type pointF "coordinates")

        public Bitmap ToDraw, BotDraw;
        public int Slowness = 0;
        private bool stopTransmitting = false, clientConnected = false, fileLoaded = false, sim = false;
        private Stream stream;
        private BluetoothClient client;
        private BluetoothAddress bluetoothAddress;
        private string fileSource;
        public PointF RestPoint;

        public Form1()
        {
            InitializeComponent();

            graphicalOverlay.Owner = this;

            ARMPointA.X = Sheet.Left + Sheet.Width + 10 * ZOOMFACTOR;
            ARMPointA.Y = Sheet.Top + Sheet.Height;

            BotDraw = ClearImage(new Bitmap(Sheet.Width, Sheet.Height));
            ToDraw = ClearImage(new Bitmap(Sheet.Width, Sheet.Height));
            Sheet.Image = ToDraw;

            const int LENGTHARM1 = 168;
            const int LENGTHARM2 = 206;

            Arm_1 = new RobotArm(LENGTHARM1 * ZOOMFACTOR, (float)Math.PI, ARMPointA.X, ARMPointA.Y);
            Arm_2 = new RobotArm(LENGTHARM2 * ZOOMFACTOR, (float)Math.PI, Arm_1.PointB.X, Arm_1.PointB.Y);

            SheetCoord = Point.Round(Arm_2.PointB);
        }


        #region Buttons

        private void StartDrawingButton_Click(object sender, EventArgs e)
        {
            try
            {
                SheetCoord = RestPoint;
                ClearImage(BotDraw);        //Preparing components
                Sheet.Image = BotDraw;
                lstbxDrawPoint.Items.Clear();
                CheckBoxDrawingMode.Checked = false;

                ToDraw = ToGreyLevels(ToDraw);      //Traming image

                DrawPointList = SortByDistance(DrawPointList);          //Organize the point to make the robot efficient

                foreach (PixelPointF P in DrawPointList)
                {
                    IEnumerable<Point> Line = GetPointsOnLine(Convert.ToInt32(SheetCoord.X), Convert.ToInt32(SheetCoord.Y), Convert.ToInt32(P.Coordinates.X), Convert.ToInt32(P.Coordinates.Y));

                    if (Math.Abs(SheetCoord.X - Line.First().X) < 1 || Math.Abs(SheetCoord.Y - Line.First().Y) < 1)
                    {
                        foreach (Point PTransition in Line)
                        {
                            SheetCoord = new Point(PTransition.X, PTransition.Y);

                            if (CheckBoxDrawArm.Checked == true)
                            {
                                System.Threading.Thread.Sleep(Slowness); //param the speed
                                CalculateArm(SheetCoord);
                            }
                            else
                            {
                                Sheet.Refresh();
                                pctboxRobotArms.Refresh();
                                CalculateArm(new Point(Sheet.Width, Sheet.Height));
                            }
                        }
                    }

                    else
                    {
                        foreach (Point PTransition in Line.Reverse())
                        {
                            SheetCoord = new Point(PTransition.X, PTransition.Y);

                            if (CheckBoxDrawArm.Checked == true)
                            {
                                System.Threading.Thread.Sleep(Slowness); //param the speed
                                CalculateArm(SheetCoord);
                            }
                            else
                            {
                                Sheet.Refresh();
                                pctboxRobotArms.Refresh();
                                CalculateArm(new Point(Sheet.Width, Sheet.Height));
                            }
                        }
                    }

                    SheetCoord = P.Coordinates;
                    BotDraw.SetPixel((Int32)(SheetCoord.X), (Int32)(SheetCoord.Y), Color.Black);
                    Sheet.Refresh();

                    StartDrawingButton.Enabled = false;
                    ImportImageButton.Enabled = false;
                    btnImportList.Enabled = false;

                }
            }
            catch
            {
                MessageBox.Show("There is nothing to draw at the moment", "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }

        }

        private void Sheet_MouseMove(object sender, MouseEventArgs e)
        {
            if (CheckBoxDrawingMode.Checked == true)
            {
                SheetCoord = Sheet.PointToClient(Cursor.Position);

                if (e.Button == MouseButtons.Left && SheetCoord.X > 0 && SheetCoord.X < Sheet.Width && SheetCoord.Y > 0 && SheetCoord.Y < Sheet.Height)
                {
                    ToDraw.SetPixel((int)SheetCoord.X, (int)SheetCoord.Y, Color.Black);

                    lstbxDrawPoint.Items.Add(new PixelPointF(new PointF(SheetCoord.X, SheetCoord.Y), true));
                    DrawPointList.Add(new PixelPointF(new PointF(SheetCoord.X, SheetCoord.Y), true));
                }

                if (CheckBoxDrawArm.Checked == true)
                {
                    CalculateArm(SheetCoord);
                }
                else
                {
                    Sheet.Refresh();
                    pctboxRobotArms.Refresh();
                    CalculateArm(new Point(Sheet.Width, Sheet.Height));
                }
            }

        }
        
        private void ImportImageButton_Click(object sender, EventArgs e)
        {
            btnResetDraw_Click(this, e);
            // Wrap the creation of the OpenFileDialog instance in a using statement,
            // rather than manually calling the Dispose method to ensure proper disposal
            using (OpenFileDialog dlg = new OpenFileDialog())
            {
                dlg.Title = "Open Image";
                dlg.Filter = "Image files (*.jpg, *.jpeg, *.jpe, *.jfif, *.png) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png";

                if (dlg.ShowDialog() == DialogResult.OK)
                {
                    // Create a new Bitmap object from the picture file on disk,
                    // and assign that to the PictureBox.Image property
                    Bitmap temp = new Bitmap(dlg.FileName);

                    if (temp.Width > Sheet.Width || temp.Height > Sheet.Height)
                    {
                        MessageBox.Show("Image is too big to fit on the sheet", "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                    }
                    else
                    {
                        ToDraw = temp;
                        ToDraw = ToGreyLevels(ToDraw);      //Traming image
                        DrawPointList = SortByDistance(DrawPointList);          //Organize the point to make the robot efficient

                        foreach (PixelPointF P in DrawPointList)
                        {
                            lstbxDrawPoint.Items.Add(P);
                        }
                    }
                }
            }
        }

        private void btnResetDraw_Click(object sender, EventArgs e)
        {
            ClearImage(BotDraw);
            ClearImage(ToDraw);
            Sheet.Image = ToDraw;
            DrawPointList.Clear();
            lstbxDrawPoint.Items.Clear();
            StartDrawingButton.Enabled = true;
            ImportImageButton.Enabled = true;
            btnImportList.Enabled = true;
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            if (lstbxDrawPoint.Items.Count != 0)
            {
                var saveFileDialog1 = new SaveFileDialog
                {
                    InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.Personal),
                    Filter = string.Format("{0}Text files (*.txt)|*.txt|All files (*.*)|*.*", "ARG0"),
                    RestoreDirectory = true,
                    ShowHelp = true,
                    CheckFileExists = false
                };

                if (saveFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    bool isPenUp = true;

                    File.AppendAllText(saveFileDialog1.FileName, string.Format("M4 0.OK\r\nM10 \r\n", Environment.NewLine));

                    for (int i = 0; i < DrawPointList.Count() - 1; i++)
                    {
                        File.AppendAllText(saveFileDialog1.FileName, string.Format(".G1 X-" + (DrawPointList[i].Coordinates.X/3).ToString("######.00") + " Y" + (DrawPointList[i].Coordinates.Y/3).ToString("######.00") + " A0.OK\r\n", Environment.NewLine));

                        if (isPenUp == true)
                        {
                            File.AppendAllText(saveFileDialog1.FileName, string.Format(".M1 80.OK\r\n", Environment.NewLine));
                            isPenUp = false;
                        }

                        if (Math.Abs(DrawPointList[i].Coordinates.X/3) - Math.Abs(DrawPointList[i + 1].Coordinates.X/3) > 1 || Math.Abs(DrawPointList[i].Coordinates.Y/3) - Math.Abs(DrawPointList[i + 1].Coordinates.Y/3) > 1)
                        {
                            File.AppendAllText(saveFileDialog1.FileName, string.Format(".M1 120.OK\r\n", Environment.NewLine));
                            isPenUp = true;
                        }
                    }

                    File.AppendAllText(saveFileDialog1.FileName, string.Format(".G1 X-" + (DrawPointList[DrawPointList.Count() - 1].Coordinates.X/3).ToString("######.00") + " Y" + (DrawPointList[DrawPointList.Count() - 1].Coordinates.Y/3).ToString("######.00") + " A0.OK\r\n", Environment.NewLine));
                    File.AppendAllText(saveFileDialog1.FileName, string.Format(".M1 120.OK\r\n.", Environment.NewLine));
                    isPenUp = true;
                }
            }
            else
            {
                MessageBox.Show("There is nothing to save at the moment", "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        private void btnImportList_Click(object sender, EventArgs e)
        {
            btnResetDraw_Click(this, e);
            // Wrap the creation of the OpenFileDialog instance in a using statement,
            // rather than manually calling the Dispose method to ensure proper disposal
            using (OpenFileDialog dlg = new OpenFileDialog())
            {
                dlg.Title = "Open Liste";
                dlg.Filter = "Text files (*.txt) | *.txt";

                if (dlg.ShowDialog() == DialogResult.OK)
                {
                    fileSource = dlg.FileName;
                    // Create a new Bitmap object from the picture file on disk,
                    // and assign that to the PictureBox.Image property DrawPointList.Clear();
                    using (StreamReader sr = new StreamReader(dlg.FileName))
                    {
                        string sor = ""; ;
                        string[] r = new string[4];
                        while (!sr.EndOfStream)
                        {
                            sor = sr.ReadLine();
                            r = sor.Split(' ');
                            if (sor.StartsWith(".G1"))
                            {
                                DrawPointList.Add(new PixelPointF(new PointF(float.Parse(r[1].Substring(2)), float.Parse(r[2].Substring(1))), true));
                                lstbxDrawPoint.Items.Add(DrawPointList.Last());
                            }
                        }
                    }
                }
            }
        }

        private void btnSendScara_Click_1(object sender, EventArgs e)
        { // send data blootooth
            lstbxDrawPoint.Items.Clear();
            Application.DoEvents();
            stopTransmitting = false;
            sim = false;
            //btnCancelTask.Show();
            //btnCancelTask.Enabled = true;

            stream = client.GetStream();
            stream.ReadTimeout = 10000;

            StreamReader file = new StreamReader(fileSource, true);
            string strLine = "";

            new Thread(delegate () {
                do
                {
                    //Lit la ligne dans le fichier texte
                    strLine = file.ReadLine();
                    if (strLine == "" || strLine == null || strLine == ".")
                    {
                        break;
                    }
                    if (strLine.StartsWith("."))
                    {
                        strLine = strLine.Substring(1);
                    }

                    strLine += (char)10;

                    //Envoi la ligne au robot
                    byte[] msg = Encoding.ASCII.GetBytes(strLine);
                    if (!stopTransmitting)
                    {
                        stream.Write(msg, 0, msg.Length);
                    }
                    byte[] rsp = new byte[128];
                    string msgOK;
                    //attend que le robot réponde
                    if (!stopTransmitting)
                    {
                        do
                        {
                            try
                            {
                                rsp = new byte[128];
                                stream.Read(rsp, 0, 128);
                            }
                            catch
                            {
                                Debug.WriteLine("Pas de message");
                            }
                            msgOK = "";
                            msgOK = Encoding.ASCII.GetString(rsp);
                            Debug.WriteLine(msgOK);
                        } while (!msgOK.Contains("OK") && !msgOK.Contains("ok") && !stopTransmitting);

                        if (!stopTransmitting)
                        {
                            //écriture des logs
                            Invoke((MethodInvoker)delegate {
                                // Running on the UI thread
                                //log = data + "." + verifReturn;
                                string log = "";
                                log = strLine + " ; " + msgOK;
                                lstbxDrawPoint.Items.Add(log);
                                //scroll automatique du listbox -- le clignotement vient d'ici !
                                int nItems = (int)(lstbxDrawPoint.Height / lstbxDrawPoint.ItemHeight);
                                lstbxDrawPoint.TopIndex = lstbxDrawPoint.Items.Count - nItems;
                            });
                        }
                    }
                }

                while (strLine != "." && strLine != "" && strLine != null && !stopTransmitting);

                file.Close();
                if (!stopTransmitting)
                {
                    //stream.Close();
                    Invoke((MethodInvoker)delegate {
                        // Running on the UI thread
                        //btnCancelTask.Hide();
                    });
                    MessageBox.Show("Dessin Terminé.", "Information", MessageBoxButtons.OK);
                }

            }).Start();
        }
        
        private void btnBluetooth_Click_1(object sender, EventArgs e)
        { // connexion
            client = new BluetoothClient();

            SelectBluetoothDeviceDialog sbdd = new SelectBluetoothDeviceDialog();
            sbdd.ShowUnknown = true;
            sbdd.ShowRemembered = false;
            sbdd.ShowAuthenticated = true;
            if (sbdd.ShowDialog() == DialogResult.OK)
            {

                //connecter perif, doit être pairer avant
                if (sbdd.SelectedDevice.Authenticated)
                {
                    Debug.WriteLine("Authenticated");
                    bluetoothAddress = sbdd.SelectedDevice.DeviceAddress;
                    client = new BluetoothClient();

                    BluetoothEndPoint ep = new BluetoothEndPoint(bluetoothAddress, BluetoothService.SerialPort);
                    try
                    {

                        Cursor.Current = Cursors.WaitCursor;

                        client.Connect(ep);
                        clientConnected = true;
                        if (clientConnected && fileLoaded)
                        {
                            btnSendScara.Enabled = true;
                        }
                        Debug.WriteLine("Connected");

                        Cursor.Current = Cursors.Arrow;
                        btnBluetooth.ForeColor = Color.Green;

                    }
                    catch
                    {

                        Cursor.Current = Cursors.Arrow;

                        MessageBox.Show("Device not *LISTENING*", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }


                    //client.Close();

                }
                else
                {
                    MessageBox.Show("Device not paired", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }

            }
        }


        #endregion

        #region Drawing functions

        private bool CalculateArm(PointF SheetCoord)
        {
            SheetCoord.X += Sheet.Left;
            SheetCoord.Y += Sheet.Top;

            int nbIntersections = FindCircleCircleIntersections((float)SheetCoord.X, (float)SheetCoord.Y, (float)Arm_2.armLength, Arm_1.PointA.X, Arm_1.PointA.Y, (float)Arm_1.armLength, out i1, out i2);

            Arm_1.PointB = i1;
            Arm_2.PointA = Arm_1.PointB;
            Arm_2.PointB = SheetCoord;
            
            Sheet.Refresh();
            pctboxRobotArms.Refresh();

            Application.DoEvents();
            return false;
        }
        
        private Bitmap ToGreyLevels(Bitmap original)
        {
            //Function from http://stackoverflow.com/users/472875/user472875 modified to fit my needs

            Bitmap output = new Bitmap(original.Width, original.Height);

            for (int i = 0; i < original.Width; i++)
            {

                for (int j = 0; j < original.Height; j++)
                {

                    Color c = original.GetPixel(i, j);

                    double average = ((c.R + c.B + c.G) / 3);

                    switch (Convert.ToInt32(Math.Floor((average / 64))))
                    {
                        case 2:
                            {
                                if (i % 2 == 0 && j % 2 == 0)
                                {
                                    output.SetPixel(i, j, Color.Black);
                                    DrawPointList.Add(new PixelPointF(new PointF(i, j)));
                                }
                                break;
                            }
                        case 1:
                            {
                                if (i % 2 == 0)
                                {
                                    output.SetPixel(i, j, Color.Black);
                                    DrawPointList.Add(new PixelPointF(new PointF(i, j)));
                                }
                                break;
                            }
                        case 0:
                            {
                                output.SetPixel(i, j, Color.Black);
                                DrawPointList.Add(new PixelPointF(new PointF(i, j)));
                                break;
                            }
                        default:
                            {
                            }
                            break;

                    }

                }
            }

            return output;
        }

        private Bitmap ClearImage(Bitmap ToClear)
        {
            for (int i = 0; i < ToClear.Width; i++)
            {
                for (int ii = 0; ii < ToClear.Height; ii++)
                {
                    ToClear.SetPixel(i, ii, Color.White);
                }
            }
            return ToClear;
        }

        private void graphicalOverlay_Paint(object sender, PaintEventArgs e)
        {
            Pen pen;
            pen = new Pen(Color.Red, 5);

            Rectangle rect = this.ClientRectangle;
            rect.Inflate(-10, -10);

            pen = new Pen(Color.Red, 3);
            e.Graphics.DrawLine(pen, Arm_1.PointA.X, Arm_1.PointA.Y, Arm_1.PointB.X, Arm_1.PointB.Y);
            pen = new Pen(Color.Blue, 3);
            e.Graphics.DrawLine(pen, Arm_2.PointA.X, Arm_2.PointA.Y, Arm_2.PointB.X, Arm_2.PointB.Y);

            //pen.Dispose();
            //e.Dispose();
        }

        

        private void nUPSlowness_ValueChanged(object sender, EventArgs e)
        {
            Slowness = (Int32)nUDSlowness.Value*5;
        }

        #endregion


        #region Algorithmes

        public static IEnumerable<Point> GetPointsOnLine(int x0, int y0, int x1, int y1)
        {
            bool steep = Math.Abs(y1 - y0) > Math.Abs(x1 - x0);
            if (steep)
            {
                int t;
                t = x0; // swap x0 and y0
                x0 = y0;
                y0 = t;
                t = x1; // swap x1 and y1
                x1 = y1;
                y1 = t;
            }
            if (x0 > x1)
            {
                int t;
                t = x0; // swap x0 and x1
                x0 = x1;
                x1 = t;
                t = y0; // swap y0 and y1
                y0 = y1;
                y1 = t;
            }
            int dx = x1 - x0;
            int dy = Math.Abs(y1 - y0);
            int error = dx / 2;
            int ystep = (y0 < y1) ? 1 : -1;
            int y = y0;
            for (int x = x0; x <= x1; x++)
            {
                yield return new Point((steep ? y : x), (steep ? x : y));
                error = error - dy;
                if (error < 0)
                {
                    y += ystep;
                    error += dx;
                }
            }
            yield break;
        }

        private int FindCircleCircleIntersections(float cx0, float cy0, float radius0, float cx1, float cy1, float radius1, out PointF intersection1, out PointF intersection2)
        {
            // Find the distance between the centers.
            float dx = cx0 - cx1;
            float dy = cy0 - cy1;
            double dist = Math.Sqrt(dx * dx + dy * dy);

            // See how many solutions there are.
            if (dist > radius0 + radius1)
            {
                // No solutions, the circles are too far apart.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if (dist < Math.Abs(radius0 - radius1))
            {
                // No solutions, one circle contains the other.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if ((dist == 0) && (radius0 == radius1))
            {
                // No solutions, the circles coincide.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else
            {
                // Find a and h.
                double a = (radius0 * radius0 - radius1 * radius1 + dist * dist) / (2 * dist);
                double h = Math.Sqrt(radius0 * radius0 - a * a);

                // Find P2.
                double cx2 = cx0 + a * (cx1 - cx0) / dist;
                double cy2 = cy0 + a * (cy1 - cy0) / dist;

                // Get the points P3.
                intersection1 = new PointF(
                    (float)(cx2 + h * (cy1 - cy0) / dist),
                    (float)(cy2 - h * (cx1 - cx0) / dist));
                intersection2 = new PointF(
                    (float)(cx2 - h * (cy1 - cy0) / dist),
                    (float)(cy2 + h * (cx1 - cx0) / dist));

                // See if we have 1 or 2 solutions.
                if (dist == radius0 + radius1) return 1;
                return 2;
            }
        }

        private List<PixelPointF> SortByDistance(List<PixelPointF> lst)
        {
            List<PixelPointF> output = new List<PixelPointF>();
            output.Add(lst[NearestPoint(new PixelPointF(new PointF(0, 0), false), lst)]);
            lst.Remove(output[0]);
            int x = 0;
            for (int i = 0; i < lst.Count + x; i++)
            {
                output.Add(lst[NearestPoint(output[output.Count - 1], lst)]);
                lst.Remove(output[output.Count - 1]);
                x++;

                progressBarProcessing.Maximum = lst.Count() + x + 1;
                progressBarProcessing.Value = x;

                Application.DoEvents();
            }
            return output;
        }
        
        private int NearestPoint(PixelPointF srcPt, List<PixelPointF> lookIn)
        {
            KeyValuePair<double, int> smallestDistance = new KeyValuePair<double, int>();
            for (int i = 0; i < lookIn.Count; i++)
            {
                double distance = Math.Sqrt(Math.Pow(srcPt.Coordinates.X - lookIn[i].Coordinates.X, 2) + Math.Pow(srcPt.Coordinates.Y - lookIn[i].Coordinates.Y, 2));
                if (i == 0)
                {
                    smallestDistance = new KeyValuePair<double, int>(distance, i);
                }
                else
                {
                    if (distance < smallestDistance.Key)
                    {
                        smallestDistance = new KeyValuePair<double, int>(distance, i);
                    }
                }
            }
            return smallestDistance.Value;
        }

        #endregion
    }
}

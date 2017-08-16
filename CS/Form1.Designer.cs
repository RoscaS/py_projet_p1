namespace drawing_robot_simulator
{
    partial class Form1
    {
        /// <summary>
        /// Variable nécessaire au concepteur.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Nettoyage des ressources utilisées.
        /// </summary>
        /// <param name="disposing">true si les ressources managées doivent être supprimées ; sinon, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Code généré par le Concepteur Windows Form

        /// <summary>
        /// Méthode requise pour la prise en charge du concepteur - ne modifiez pas
        /// le contenu de cette méthode avec l'éditeur de code.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.Sheet = new System.Windows.Forms.PictureBox();
            this.StartDrawingButton = new System.Windows.Forms.Button();
            this.CheckBoxDrawingMode = new System.Windows.Forms.CheckBox();
            this.ImportImageButton = new System.Windows.Forms.Button();
            this.CheckBoxDrawArm = new System.Windows.Forms.CheckBox();
            this.btnResetDraw = new System.Windows.Forms.Button();
            this.progressBarProcessing = new System.Windows.Forms.ProgressBar();
            this.btnSave = new System.Windows.Forms.Button();
            this.btnImportList = new System.Windows.Forms.Button();
            this.lstbxDrawPoint = new System.Windows.Forms.ListBox();
            this.pctboxRobotArms = new System.Windows.Forms.PictureBox();
            this.nUDSlowness = new System.Windows.Forms.NumericUpDown();
            this.lblRakenti = new System.Windows.Forms.Label();
            this.graphicalOverlay = new CodeProject.GraphicalOverlay(this.components);
            this.btnSendScara = new System.Windows.Forms.Button();
            this.btnBluetooth = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.Sheet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pctboxRobotArms)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nUDSlowness)).BeginInit();
            this.SuspendLayout();
            // 
            // Sheet
            // 
            this.Sheet.BackColor = System.Drawing.Color.Transparent;
            this.Sheet.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.Sheet.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.Sheet.Location = new System.Drawing.Point(18, 18);
            this.Sheet.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Sheet.Name = "Sheet";
            this.Sheet.Size = new System.Drawing.Size(891, 630);
            this.Sheet.TabIndex = 0;
            this.Sheet.TabStop = false;
            this.Sheet.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Sheet_MouseMove);
            // 
            // StartDrawingButton
            // 
            this.StartDrawingButton.Location = new System.Drawing.Point(176, 740);
            this.StartDrawingButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.StartDrawingButton.Name = "StartDrawingButton";
            this.StartDrawingButton.Size = new System.Drawing.Size(148, 35);
            this.StartDrawingButton.TabIndex = 9;
            this.StartDrawingButton.TabStop = false;
            this.StartDrawingButton.Text = "Draw";
            this.StartDrawingButton.UseVisualStyleBackColor = true;
            this.StartDrawingButton.Click += new System.EventHandler(this.StartDrawingButton_Click);
            // 
            // CheckBoxDrawingMode
            // 
            this.CheckBoxDrawingMode.AutoSize = true;
            this.CheckBoxDrawingMode.Location = new System.Drawing.Point(428, 746);
            this.CheckBoxDrawingMode.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.CheckBoxDrawingMode.Name = "CheckBoxDrawingMode";
            this.CheckBoxDrawingMode.Size = new System.Drawing.Size(137, 24);
            this.CheckBoxDrawingMode.TabIndex = 7;
            this.CheckBoxDrawingMode.Text = "Drawing Mode";
            this.CheckBoxDrawingMode.UseVisualStyleBackColor = true;
            // 
            // ImportImageButton
            // 
            this.ImportImageButton.Location = new System.Drawing.Point(18, 740);
            this.ImportImageButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.ImportImageButton.Name = "ImportImageButton";
            this.ImportImageButton.Size = new System.Drawing.Size(148, 35);
            this.ImportImageButton.TabIndex = 12;
            this.ImportImageButton.Text = "Import Image";
            this.ImportImageButton.UseVisualStyleBackColor = true;
            this.ImportImageButton.Click += new System.EventHandler(this.ImportImageButton_Click);
            // 
            // CheckBoxDrawArm
            // 
            this.CheckBoxDrawArm.AutoSize = true;
            this.CheckBoxDrawArm.Checked = true;
            this.CheckBoxDrawArm.CheckState = System.Windows.Forms.CheckState.Checked;
            this.CheckBoxDrawArm.Location = new System.Drawing.Point(428, 791);
            this.CheckBoxDrawArm.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.CheckBoxDrawArm.Name = "CheckBoxDrawArm";
            this.CheckBoxDrawArm.Size = new System.Drawing.Size(113, 24);
            this.CheckBoxDrawArm.TabIndex = 13;
            this.CheckBoxDrawArm.Text = "Draw Arms";
            this.CheckBoxDrawArm.UseVisualStyleBackColor = true;
            // 
            // btnResetDraw
            // 
            this.btnResetDraw.Location = new System.Drawing.Point(177, 785);
            this.btnResetDraw.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btnResetDraw.Name = "btnResetDraw";
            this.btnResetDraw.Size = new System.Drawing.Size(148, 35);
            this.btnResetDraw.TabIndex = 14;
            this.btnResetDraw.Text = "Reset Drawing";
            this.btnResetDraw.UseVisualStyleBackColor = true;
            this.btnResetDraw.Click += new System.EventHandler(this.btnResetDraw_Click);
            // 
            // progressBarProcessing
            // 
            this.progressBarProcessing.Location = new System.Drawing.Point(17, 919);
            this.progressBarProcessing.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.progressBarProcessing.Name = "progressBarProcessing";
            this.progressBarProcessing.Size = new System.Drawing.Size(308, 35);
            this.progressBarProcessing.TabIndex = 15;
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(18, 829);
            this.btnSave.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(148, 35);
            this.btnSave.TabIndex = 16;
            this.btnSave.Text = "Save List ";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // btnImportList
            // 
            this.btnImportList.Location = new System.Drawing.Point(18, 785);
            this.btnImportList.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btnImportList.Name = "btnImportList";
            this.btnImportList.Size = new System.Drawing.Size(148, 35);
            this.btnImportList.TabIndex = 18;
            this.btnImportList.Text = "Import List";
            this.btnImportList.UseVisualStyleBackColor = true;
            this.btnImportList.Click += new System.EventHandler(this.btnImportList_Click);
            // 
            // lstbxDrawPoint
            // 
            this.lstbxDrawPoint.FormattingEnabled = true;
            this.lstbxDrawPoint.ItemHeight = 20;
            this.lstbxDrawPoint.Location = new System.Drawing.Point(628, 740);
            this.lstbxDrawPoint.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.lstbxDrawPoint.Name = "lstbxDrawPoint";
            this.lstbxDrawPoint.Size = new System.Drawing.Size(278, 164);
            this.lstbxDrawPoint.TabIndex = 19;
            // 
            // pctboxRobotArms
            // 
            this.pctboxRobotArms.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pctboxRobotArms.Location = new System.Drawing.Point(3, 3);
            this.pctboxRobotArms.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.pctboxRobotArms.Name = "pctboxRobotArms";
            this.pctboxRobotArms.Size = new System.Drawing.Size(1504, 714);
            this.pctboxRobotArms.TabIndex = 20;
            this.pctboxRobotArms.TabStop = false;
            // 
            // nUDSlowness
            // 
            this.nUDSlowness.Location = new System.Drawing.Point(510, 834);
            this.nUDSlowness.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.nUDSlowness.Name = "nUDSlowness";
            this.nUDSlowness.Size = new System.Drawing.Size(54, 26);
            this.nUDSlowness.TabIndex = 21;
            this.nUDSlowness.ValueChanged += new System.EventHandler(this.nUPSlowness_ValueChanged);
            // 
            // lblRakenti
            // 
            this.lblRakenti.AutoSize = true;
            this.lblRakenti.Location = new System.Drawing.Point(423, 837);
            this.lblRakenti.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblRakenti.Name = "lblRakenti";
            this.lblRakenti.Size = new System.Drawing.Size(77, 20);
            this.lblRakenti.TabIndex = 22;
            this.lblRakenti.Text = "Slowness";
            // 
            // graphicalOverlay
            // 
            this.graphicalOverlay.Paint += new System.EventHandler<System.Windows.Forms.PaintEventArgs>(this.graphicalOverlay_Paint);
            // 
            // btnSendScara
            // 
            this.btnSendScara.Location = new System.Drawing.Point(178, 829);
            this.btnSendScara.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btnSendScara.Name = "btnSendScara";
            this.btnSendScara.Size = new System.Drawing.Size(148, 35);
            this.btnSendScara.TabIndex = 23;
            this.btnSendScara.Text = "Send to bot";
            this.btnSendScara.UseVisualStyleBackColor = true;
            this.btnSendScara.Click += new System.EventHandler(this.btnSendScara_Click_1);
            // 
            // btnBluetooth
            // 
            this.btnBluetooth.Location = new System.Drawing.Point(18, 874);
            this.btnBluetooth.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btnBluetooth.Name = "btnBluetooth";
            this.btnBluetooth.Size = new System.Drawing.Size(148, 35);
            this.btnBluetooth.TabIndex = 24;
            this.btnBluetooth.Text = "Bluetooth";
            this.btnBluetooth.UseVisualStyleBackColor = true;
            this.btnBluetooth.Click += new System.EventHandler(this.btnBluetooth_Click_1);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1526, 1046);
            this.Controls.Add(this.btnBluetooth);
            this.Controls.Add(this.btnSendScara);
            this.Controls.Add(this.lblRakenti);
            this.Controls.Add(this.nUDSlowness);
            this.Controls.Add(this.Sheet);
            this.Controls.Add(this.pctboxRobotArms);
            this.Controls.Add(this.lstbxDrawPoint);
            this.Controls.Add(this.btnImportList);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.progressBarProcessing);
            this.Controls.Add(this.btnResetDraw);
            this.Controls.Add(this.CheckBoxDrawArm);
            this.Controls.Add(this.ImportImageButton);
            this.Controls.Add(this.CheckBoxDrawingMode);
            this.Controls.Add(this.StartDrawingButton);
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Form1";
            this.Text = "Drawing Robot Simulator";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.Sheet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pctboxRobotArms)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nUDSlowness)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox Sheet;
        private System.Windows.Forms.Button StartDrawingButton;
        private CodeProject.GraphicalOverlay graphicalOverlay;
        private System.Windows.Forms.CheckBox CheckBoxDrawingMode;
        private System.Windows.Forms.Button ImportImageButton;
        private System.Windows.Forms.CheckBox CheckBoxDrawArm;
        private System.Windows.Forms.Button btnResetDraw;
        private System.Windows.Forms.ProgressBar progressBarProcessing;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.Button btnImportList;
        private System.Windows.Forms.ListBox lstbxDrawPoint;
        private System.Windows.Forms.PictureBox pctboxRobotArms;
        private System.Windows.Forms.NumericUpDown nUDSlowness;
        private System.Windows.Forms.Label lblRakenti;
        private System.Windows.Forms.Button btnSendScara;
        private System.Windows.Forms.Button btnBluetooth;
    }
}


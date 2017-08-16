using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace drawing_robot_simulator
{
    public class PixelPointF
    {
        #region Attributes

        private PointF coordinates;
        private bool penEngaged;

        #endregion

        #region Properties

        public PointF Coordinates
        {
            get
            {
                return this.coordinates;
            }
            set
            {
                this.coordinates = value;
            }
        }

        public bool PenEngaged
        {
            get
            {
                return this.penEngaged;
            }
            set
            {
                this.penEngaged = value;
            }
        }

        #endregion

        #region Methods



        #endregion

        #region Constructor

        // Default Constructor
        public PixelPointF()
        {
            coordinates = new PointF(0, 0);
            penEngaged = false;
        }

        // Specific point constructor
        public PixelPointF(PointF Coordinates, bool PenEngaged = false)
        {
            coordinates = Coordinates;
            penEngaged = PenEngaged;
        }

        #endregion

    }
}

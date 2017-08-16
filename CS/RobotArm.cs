using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Threading.Tasks;

namespace drawing_robot_simulator
{
    public class RobotArm
    {
        #region Attributes

        public double armLength;
        public double armAngle;
        public PointF PointA;
        public PointF PointB;


        #endregion


        #region Properties

        //public double ArmAngle  //To prevent from entering invalide value.
        //{
        //    get
        //    {
        //        return armAngle;
        //    }
        //    set
        //    {
        //        while (!(ArmAngle <= 360 || ArmAngle <= 0))     //To avoid angle such as 720°
        //        {
        //            if (ArmAngle < 0)
        //            {
        //                ArmAngle += 360;
        //            }
        //            else
        //            {
        //                ArmAngle -= 360;
        //            }
        //        }

        //        armAngle = ArmAngle;
        //    }
        //}

        #endregion


        #region Methods

        public void CalculateAngles()
        {
            armAngle = Math.Atan2(PointA.Y - PointB.Y, PointA.X - PointB.X);
        }

        #endregion


        #region Builders

        public RobotArm(float ArmLenght, float ArmAngle, float BaseAxisX, float BaseAxisY)
        {
            armLength = ArmLenght;
            armAngle = ArmAngle;
            PointA.X = BaseAxisX;
            PointA.Y = BaseAxisY;
            PointB.X = BaseAxisX + (float)Math.Cos(ArmAngle) * ArmLenght;
            PointB.Y = BaseAxisY + (float)Math.Sin(ArmAngle) * ArmLenght;
    }

        #endregion

    }
}

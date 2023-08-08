;; Auto-generated. Do not edit!


(when (boundp 'rasbot_msgs::DriveMsg)
  (if (not (find-package "RASBOT_MSGS"))
    (make-package "RASBOT_MSGS"))
  (shadow 'DriveMsg (find-package "RASBOT_MSGS")))
(unless (find-package "RASBOT_MSGS::DRIVEMSG")
  (make-package "RASBOT_MSGS::DRIVEMSG"))

(in-package "ROS")
;;//! \htmlinclude DriveMsg.msg.html


(defclass rasbot_msgs::DriveMsg
  :super ros::object
  :slots (_left _right ))

(defmethod rasbot_msgs::DriveMsg
  (:init
   (&key
    ((:left __left) 0)
    ((:right __right) 0)
    )
   (send-super :init)
   (setq _left (round __left))
   (setq _right (round __right))
   self)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:serialization-length
   ()
   (+
    ;; int32 _left
    4
    ;; int32 _right
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _left
       (write-long _left s)
     ;; int32 _right
       (write-long _right s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _left
     (setq _left (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _right
     (setq _right (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get rasbot_msgs::DriveMsg :md5sum-) "febc810ab9cc360ca3f47fcee4f2ba71")
(setf (get rasbot_msgs::DriveMsg :datatype-) "rasbot_msgs/DriveMsg")
(setf (get rasbot_msgs::DriveMsg :definition-)
      "int32 left
int32 right

")



(provide :rasbot_msgs/DriveMsg "febc810ab9cc360ca3f47fcee4f2ba71")



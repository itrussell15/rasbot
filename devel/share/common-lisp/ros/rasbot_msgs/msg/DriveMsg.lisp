; Auto-generated. Do not edit!


(cl:in-package rasbot_msgs-msg)


;//! \htmlinclude DriveMsg.msg.html

(cl:defclass <DriveMsg> (roslisp-msg-protocol:ros-message)
  ((left
    :reader left
    :initarg :left
    :type cl:integer
    :initform 0)
   (right
    :reader right
    :initarg :right
    :type cl:integer
    :initform 0))
)

(cl:defclass DriveMsg (<DriveMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DriveMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DriveMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rasbot_msgs-msg:<DriveMsg> is deprecated: use rasbot_msgs-msg:DriveMsg instead.")))

(cl:ensure-generic-function 'left-val :lambda-list '(m))
(cl:defmethod left-val ((m <DriveMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rasbot_msgs-msg:left-val is deprecated.  Use rasbot_msgs-msg:left instead.")
  (left m))

(cl:ensure-generic-function 'right-val :lambda-list '(m))
(cl:defmethod right-val ((m <DriveMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rasbot_msgs-msg:right-val is deprecated.  Use rasbot_msgs-msg:right instead.")
  (right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DriveMsg>) ostream)
  "Serializes a message object of type '<DriveMsg>"
  (cl:let* ((signed (cl:slot-value msg 'left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'right)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DriveMsg>) istream)
  "Deserializes a message object of type '<DriveMsg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'left) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'right) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DriveMsg>)))
  "Returns string type for a message object of type '<DriveMsg>"
  "rasbot_msgs/DriveMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DriveMsg)))
  "Returns string type for a message object of type 'DriveMsg"
  "rasbot_msgs/DriveMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DriveMsg>)))
  "Returns md5sum for a message object of type '<DriveMsg>"
  "febc810ab9cc360ca3f47fcee4f2ba71")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DriveMsg)))
  "Returns md5sum for a message object of type 'DriveMsg"
  "febc810ab9cc360ca3f47fcee4f2ba71")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DriveMsg>)))
  "Returns full string definition for message of type '<DriveMsg>"
  (cl:format cl:nil "int32 left~%int32 right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DriveMsg)))
  "Returns full string definition for message of type 'DriveMsg"
  (cl:format cl:nil "int32 left~%int32 right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DriveMsg>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DriveMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'DriveMsg
    (cl:cons ':left (left msg))
    (cl:cons ':right (right msg))
))

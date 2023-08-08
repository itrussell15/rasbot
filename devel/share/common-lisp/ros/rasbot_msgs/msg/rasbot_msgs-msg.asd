
(cl:in-package :asdf)

(defsystem "rasbot_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DriveMsg" :depends-on ("_package_DriveMsg"))
    (:file "_package_DriveMsg" :depends-on ("_package"))
  ))
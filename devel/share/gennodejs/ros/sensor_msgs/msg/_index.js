
"use strict";

let FluidPressure = require('./FluidPressure.js');
let Temperature = require('./Temperature.js');
let RegionOfInterest = require('./RegionOfInterest.js');
let Illuminance = require('./Illuminance.js');
let CompressedImage = require('./CompressedImage.js');
let ChannelFloat32 = require('./ChannelFloat32.js');
let TimeReference = require('./TimeReference.js');
let JoyFeedbackArray = require('./JoyFeedbackArray.js');
let Range = require('./Range.js');
let BatteryState = require('./BatteryState.js');
let PointCloud = require('./PointCloud.js');
let NavSatFix = require('./NavSatFix.js');
let PointField = require('./PointField.js');
let RelativeHumidity = require('./RelativeHumidity.js');
let LaserScan = require('./LaserScan.js');
let CameraInfo = require('./CameraInfo.js');
let MultiEchoLaserScan = require('./MultiEchoLaserScan.js');
let JoyFeedback = require('./JoyFeedback.js');
let Joy = require('./Joy.js');
let MagneticField = require('./MagneticField.js');
let Image = require('./Image.js');
let MultiDOFJointState = require('./MultiDOFJointState.js');
let JointState = require('./JointState.js');
let PointCloud2 = require('./PointCloud2.js');
let LaserEcho = require('./LaserEcho.js');
let Imu = require('./Imu.js');
let NavSatStatus = require('./NavSatStatus.js');

module.exports = {
  FluidPressure: FluidPressure,
  Temperature: Temperature,
  RegionOfInterest: RegionOfInterest,
  Illuminance: Illuminance,
  CompressedImage: CompressedImage,
  ChannelFloat32: ChannelFloat32,
  TimeReference: TimeReference,
  JoyFeedbackArray: JoyFeedbackArray,
  Range: Range,
  BatteryState: BatteryState,
  PointCloud: PointCloud,
  NavSatFix: NavSatFix,
  PointField: PointField,
  RelativeHumidity: RelativeHumidity,
  LaserScan: LaserScan,
  CameraInfo: CameraInfo,
  MultiEchoLaserScan: MultiEchoLaserScan,
  JoyFeedback: JoyFeedback,
  Joy: Joy,
  MagneticField: MagneticField,
  Image: Image,
  MultiDOFJointState: MultiDOFJointState,
  JointState: JointState,
  PointCloud2: PointCloud2,
  LaserEcho: LaserEcho,
  Imu: Imu,
  NavSatStatus: NavSatStatus,
};

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: satos_payload_sdk/gen/antaris_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'satos_payload_sdk/gen/antaris_api.proto\x12\x18\x61ntaris_api_peer_to_peer\"@\n\x11\x41ntarisSdkVersion\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\r\n\x05patch\x18\x03 \x01(\x05\"\x8f\x01\n\x11ReqRegisterParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12 \n\x18health_check_fail_action\x18\x02 \x01(\x05\x12@\n\x0bsdk_version\x18\x03 \x01(\x0b\x32+.antaris_api_peer_to_peer.AntarisSdkVersion\"T\n\x12RespRegisterParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x12\n\nreq_status\x18\x02 \x01(\x05\x12\x12\n\nauth_token\x18\x03 \x01(\t\"5\n\x1bReqGetCurrentLocationParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\"\xd8\x01\n\x1cRespGetCurrentLocationParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x12\n\nreq_status\x18\x02 \x01(\x05\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x05 \x01(\x01\x12\x13\n\x0bsd_latitude\x18\x06 \x01(\x02\x12\x14\n\x0csd_longitude\x18\x07 \x01(\x02\x12\x13\n\x0bsd_altitude\x18\x08 \x01(\x02\x12\x15\n\rdetermined_at\x18\t \x01(\x03\"G\n\x1aReqStageFileDownloadParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x11\n\tfile_path\x18\x02 \x01(\t\"I\n\x1bRespStageFileDownloadParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x12\n\nreq_status\x18\x02 \x01(\x05\"O\n\x1cReqPayloadPowerControlParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x17\n\x0fpower_operation\x18\x02 \x01(\x05\"K\n\x1dRespPayloadPowerControlParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x12\n\nreq_status\x18\x02 \x01(\x05\"@\n\x12RespShutdownParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x12\n\nreq_status\x18\x02 \x01(\x05\"\x89\x01\n\x15RespHealthCheckParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x19\n\x11\x61pplication_state\x18\x02 \x01(\x05\x12\x1d\n\x15reqs_to_pc_in_err_cnt\x18\x03 \x01(\x05\x12\x1e\n\x16resps_to_pc_in_err_cnt\x18\x04 \x01(\x05\"w\n\x13StartSequenceParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x13\n\x0bsequence_id\x18\x02 \x01(\t\x12\x17\n\x0fsequence_params\x18\x03 \x01(\t\x12\x1a\n\x12scheduled_deadline\x18\x04 \x01(\x03\"<\n\x0eShutdownParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x12\n\ngrace_time\x18\x02 \x01(\x05\"\x85\x01\n\x11HealthCheckParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x19\n\x11\x61pplication_state\x18\x02 \x01(\x05\x12\x1d\n\x15reqs_to_pc_in_err_cnt\x18\x03 \x01(\x05\x12\x1e\n\x16resps_to_pc_in_err_cnt\x18\x04 \x01(\x05\"4\n\x12PayloadMetricsInfo\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\x12\r\n\x05names\x18\x02 \x01(\t\"1\n\x17ReqPayloadMetricsParams\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\"\x98\x01\n\x16PayloadMetricsResponse\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x14\n\x0cused_counter\x18\x03 \x01(\x05\x12=\n\x07metrics\x18\x04 \x03(\x0b\x32,.antaris_api_peer_to_peer.PayloadMetricsInfo\",\n\x15\x43mdSequenceDoneParams\x12\x13\n\x0bsequence_id\x18\x01 \x01(\t\".\n\x14\x41ntarisCorrelationId\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\x05\"U\n\x11\x41ntarisReturnType\x12@\n\x0breturn_code\x18\x01 \x01(\x0e\x32+.antaris_api_peer_to_peer.AntarisReturnCode*\xec\x01\n\x11\x41ntarisReturnCode\x12\x0e\n\nAn_SUCCESS\x10\x00\x12\x1f\n\x12\x41n_GENERIC_FAILURE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12\x41n_NOT_IMPLEMENTED\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x13\x41n_OUT_OF_RESOURCES\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1d\n\x10\x41n_NOT_PERMITTED\x10\xfc\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1e\n\x11\x41n_INVALID_PARAMS\x10\xfb\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x17\x41n_INCOMPATIBLE_VERSION\x10\xfa\xff\xff\xff\xff\xff\xff\xff\xff\x01\x32\x9d\x08\n\x1d\x41ntarisapiApplicationCallback\x12p\n\x10PA_StartSequence\x12-.antaris_api_peer_to_peer.StartSequenceParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12i\n\x0ePA_ShutdownApp\x12(.antaris_api_peer_to_peer.ShutdownParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12s\n\x15PA_ProcessHealthCheck\x12+.antaris_api_peer_to_peer.HealthCheckParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12y\n\x1aPA_ProcessResponseRegister\x12,.antaris_api_peer_to_peer.RespRegisterParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12\x8d\x01\n$PA_ProcessResponseGetCurrentLocation\x12\x36.antaris_api_peer_to_peer.RespGetCurrentLocationParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12\x8b\x01\n#PA_ProcessResponseStageFileDownload\x12\x35.antaris_api_peer_to_peer.RespStageFileDownloadParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12\x8f\x01\n%PA_ProcessResponsePayloadPowerControl\x12\x37.antaris_api_peer_to_peer.RespPayloadPowerControlParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12\x7f\n\x1bPA_ProcessReqPayloadMetrics\x12\x31.antaris_api_peer_to_peer.ReqPayloadMetricsParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x32\xf1\x07\n\x1b\x41ntarisapiPayloadController\x12i\n\x0bPC_register\x12+.antaris_api_peer_to_peer.ReqRegisterParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12\x7f\n\x17PC_get_current_location\x12\x35.antaris_api_peer_to_peer.ReqGetCurrentLocationParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12}\n\x16PC_stage_file_download\x12\x34.antaris_api_peer_to_peer.ReqStageFileDownloadParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12r\n\x10PC_sequence_done\x12/.antaris_api_peer_to_peer.CmdSequenceDoneParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12\x81\x01\n\x18PC_payload_power_control\x12\x36.antaris_api_peer_to_peer.ReqPayloadPowerControlParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12z\n\x18PC_response_health_check\x12/.antaris_api_peer_to_peer.RespHealthCheckParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12s\n\x14PC_response_shutdown\x12,.antaris_api_peer_to_peer.RespShutdownParams\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x12~\n\x1bPC_response_payload_metrics\x12\x30.antaris_api_peer_to_peer.PayloadMetricsResponse\x1a+.antaris_api_peer_to_peer.AntarisReturnType\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'satos_payload_sdk.gen.antaris_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ANTARISRETURNCODE']._serialized_start=1914
  _globals['_ANTARISRETURNCODE']._serialized_end=2150
  _globals['_ANTARISSDKVERSION']._serialized_start=69
  _globals['_ANTARISSDKVERSION']._serialized_end=133
  _globals['_REQREGISTERPARAMS']._serialized_start=136
  _globals['_REQREGISTERPARAMS']._serialized_end=279
  _globals['_RESPREGISTERPARAMS']._serialized_start=281
  _globals['_RESPREGISTERPARAMS']._serialized_end=365
  _globals['_REQGETCURRENTLOCATIONPARAMS']._serialized_start=367
  _globals['_REQGETCURRENTLOCATIONPARAMS']._serialized_end=420
  _globals['_RESPGETCURRENTLOCATIONPARAMS']._serialized_start=423
  _globals['_RESPGETCURRENTLOCATIONPARAMS']._serialized_end=639
  _globals['_REQSTAGEFILEDOWNLOADPARAMS']._serialized_start=641
  _globals['_REQSTAGEFILEDOWNLOADPARAMS']._serialized_end=712
  _globals['_RESPSTAGEFILEDOWNLOADPARAMS']._serialized_start=714
  _globals['_RESPSTAGEFILEDOWNLOADPARAMS']._serialized_end=787
  _globals['_REQPAYLOADPOWERCONTROLPARAMS']._serialized_start=789
  _globals['_REQPAYLOADPOWERCONTROLPARAMS']._serialized_end=868
  _globals['_RESPPAYLOADPOWERCONTROLPARAMS']._serialized_start=870
  _globals['_RESPPAYLOADPOWERCONTROLPARAMS']._serialized_end=945
  _globals['_RESPSHUTDOWNPARAMS']._serialized_start=947
  _globals['_RESPSHUTDOWNPARAMS']._serialized_end=1011
  _globals['_RESPHEALTHCHECKPARAMS']._serialized_start=1014
  _globals['_RESPHEALTHCHECKPARAMS']._serialized_end=1151
  _globals['_STARTSEQUENCEPARAMS']._serialized_start=1153
  _globals['_STARTSEQUENCEPARAMS']._serialized_end=1272
  _globals['_SHUTDOWNPARAMS']._serialized_start=1274
  _globals['_SHUTDOWNPARAMS']._serialized_end=1334
  _globals['_HEALTHCHECKPARAMS']._serialized_start=1337
  _globals['_HEALTHCHECKPARAMS']._serialized_end=1470
  _globals['_PAYLOADMETRICSINFO']._serialized_start=1472
  _globals['_PAYLOADMETRICSINFO']._serialized_end=1524
  _globals['_REQPAYLOADMETRICSPARAMS']._serialized_start=1526
  _globals['_REQPAYLOADMETRICSPARAMS']._serialized_end=1575
  _globals['_PAYLOADMETRICSRESPONSE']._serialized_start=1578
  _globals['_PAYLOADMETRICSRESPONSE']._serialized_end=1730
  _globals['_CMDSEQUENCEDONEPARAMS']._serialized_start=1732
  _globals['_CMDSEQUENCEDONEPARAMS']._serialized_end=1776
  _globals['_ANTARISCORRELATIONID']._serialized_start=1778
  _globals['_ANTARISCORRELATIONID']._serialized_end=1824
  _globals['_ANTARISRETURNTYPE']._serialized_start=1826
  _globals['_ANTARISRETURNTYPE']._serialized_end=1911
  _globals['_ANTARISAPIAPPLICATIONCALLBACK']._serialized_start=2153
  _globals['_ANTARISAPIAPPLICATIONCALLBACK']._serialized_end=3206
  _globals['_ANTARISAPIPAYLOADCONTROLLER']._serialized_start=3209
  _globals['_ANTARISAPIPAYLOADCONTROLLER']._serialized_end=4218
# @@protoc_insertion_point(module_scope)

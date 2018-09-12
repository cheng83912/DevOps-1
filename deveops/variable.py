# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-29
# Author Yo
# Email YoLoveLife@outlook.com

# OPS PUSH_MISSION
OPS_PUSH_MISSION_LACK_OF_KEY_OR_JUMPER = -3
OPS_PUSH_MISSION_UNREACHABLE = -2
OPS_PUSH_MISSION_FAILED = -1
OPS_PUSH_MISSION_WAIT_EXAM = 1
OPS_PUSH_MISSION_WAIT_UPLOAD = 2
OPS_PUSH_MISSION_WAIT_RUN = 3
OPS_PUSH_MISSION_RUNNING = 4
OPS_PUSH_MISSION_SUCCESS = 5
OPS_PUSH_MISSION_IMPORT_VAR = 6
OPS_PUSH_MISSION_IMPORT_TASKS = 7

# SAFE WORK
SAFEWORK_REJECT = -1
SAFEWORK_WAIT_RUN = 1
SAFEWORK_WAIT_DONE = 2
SAFEWORK_DONE = 3

# HOST
STATUS_HOST_DENY_OR_REFUSE = -4
STATUS_HOST_NOT_SELECT = -3
STATUS_HOST_CLOSE = -2
# 此状态机器将不会参与到所有运维操作中
STATUS_HOST_PAUSE = -1
STATUS_HOST_CAN_BE_USE = 1
STATUS_HOST_DISK_FULL = 2
STATUS_HOST_UPTIME_ERROR = 3

# GROUP
STATUS_GROUP_PAUSE = -2
STATUS_GROUP_UNREACHABLE = -1
STATUS_GROUP_CAN_BE_USE = 1

# JUMPER
STATUS_JUMPER_UNREACHABLE = -1
STATUS_JUMPER_CAN_BE_USE = 1

# EZSETUP STATUS
STATUS_EZSETUP_UNREACHABLE = -3
STATUS_EZSETUP_LACK_OF_KEY_OR_JUMPER = -2
STATUS_EZSETUP_ERROR = -1
STATUS_EZSETUP_INSTALLING = 1
STATUS_EZSETUP_DONE = 2

# CDN STATUS
# STATUS_CDN_ERROR_
STATUS_CDN_ERROR_BELONG = -2
STATUS_CDN_ERROR_EXISTS = -1
STATUS_CDN_RUN = 1
STATUS_CDN_DONE = 2

# CDN TYPE
TYPE_CDN_QN = 1
TYPE_CDN_WS = 2
TYPE_CDN_ALIYUN = 3

# EZSETUP TYPE
TYPE_EZSETUP_MYSQL = 1
TYPE_EZSETUP_REDIS = 2

# MONITOR TIME TYPE
TYPE_MONITOR_ONE_HOUR = 1
TYPE_MONITOR_SIX_HOUR = 2
TYPE_MONITOR_HALF_DAY = 3
TYPE_MONITOR_DAY = 4
TYPE_MONITOR_3_DAY = 5
TYPE_MONITOR_7_DAY = 6

# IP_POOL TYPE
TYPE_IP_POOL_ECS = 1
TYPE_IP_POOL_SLB = 2
TYPE_IP_POOL_DNAT = 3
TYPE_IP_POOL_SNAT = 4
TYPE_IP_POOL_WAF = 5
TYPE_IP_POOL_DDOS = 6


# DB INSTANCE
STATUS_DB_INSTANCE_CONNECT_REFUSE = -3
STATUS_DB_INSTANCE_PASSWORD_WRONG = -2
STATUS_DB_INSTANCE_UNREACHABLE = -1
STATUS_DB_INSTANCE_CAN_BE_USE = 1

# DB TYPE
TYPE_DB_INSTANCE_MASTER = 1
TYPE_DB_INSTANCE_SLAVE = 2
TYPE_DB_INSTANCE_MGR = 3


# TIMELINE
# HOST
TIMELINE_HOST_CREATE = 10
TIMELINE_HOST_UPDATE = 11
TIMELINE_HOST_DELETE = 12
TIMELINE_HOST_SORT = 13
#GROUP
TIMELINE_GROUP_CREATE = 20
TIMELINE_GROUP_UPDATE = 21
TIMELINE_GROUP_DELETE = 22
TIMELINE_GROUP_SORT = 23
# EXTENDUSER
TIMELINE_USER_CREATE = 30
TIMELINE_USER_UPDATE = 31
TIMELINE_USER_DELETE = 32
TIMELINE_USER_QRCODE = 33
# PMNGROUP
TIMELIME_PMNGROUP_CREATE = 40
TIMELINE_PMNGROUP_UPDATE = 41
TIMELINE_PMNGROUP_DELETE = 42
# KEY
TIMELINE_KEY_CREATE = 50
TIMELINE_KEY_UPDATE = 51
TIMELINE_KEY_DELETE = 52
# JUMPER
TIMELINE_JUMPER_CREATE = 60
TIMELINE_JUMPER_UPDATE = 61
TIMELINE_JUMPER_DELETE = 62
TIMELINE_JUMPER_FLUSH = 63
# META
TIMELINE_META_CREATE = 70
TIMELINE_META_UPDATE = 71
TIMELINE_META_DELETE = 72
# MISSION
TIMELINE_MISSION_CREATE = 80
TIMELINE_MISSION_UPDATE = 81
TIMELINE_MISSION_DELETE = 82
# VAR
TIMELINE_VAR_CREATE = 90
TIMELINE_VAR_UPDATE = 91
TIMELINE_VAR_DELETE = 92
# CODE WORK
TIMELINE_CODEWORK_CREATE = 100
TIMELINE_CODEWORK_EXAM = 101
TIMELINE_CODEWORK_CHECK = 102
TIMELINE_CODEWORK_UPLOAD = 103
TIMELINE_CODEWORK_RUN = 104
TIMELINE_CODEWORK_DELETE = 105
TIMELINE_CODEWORK_RESULTS = 106
# FILE
TIMELINE_UTILS_FILE_CREATE = 110
TIMELINE_UTILS_FILE_DELETE = 111
TIMELINE_UTILS_IMAGE_CREATE = 112
TIMELINE_UTILS_IMAGE_DELETE = 113
# DB
TIMELINE_DB_INSTANCE_CREATE = 120
TIMELINE_DB_INSTANCE_UPDATE = 121
TIMELINE_DB_INSTANCE_DELETE = 122
TIMELINE_DB_ROLE_CREATE = 123
TIMELINE_DB_ROLE_UPDATE = 124
TIMELINE_DB_ROLE_DELETE = 125
TIMELINE_DB_USER_CREATE = 126
TIMELINE_DB_USER_UPDATE = 127
TIMELINE_DB_USER_DELETE = 128
# SYSTYPE
TIMELINE_SYSTYPE_CREATE = 130
TIMELINE_SYSTYPE_UPDATE = 131
TIMELINE_SYSTYPE_DELETE = 132
# POSITION
TIMELINE_POSITION_CREATE = 140
TIMELINE_POSITION_UPDATE = 141
TIMELINE_POSITION_DELETE = 142
# DNS
TIMELINE_DNS_CREATE = 150
TIMELINE_DNS_UPDATE = 151
TIMELINE_DNS_DELETE = 152
# TASK
TIMELINE_TASK_EXPIRED_ECS = 160
TIMELINE_TASK_EXPIRED_RDS = 161
TIMELINE_TASK_EXPIRED_KVSTORE = 162
TIMELINE_TASK_EXPIRED_MONGODB = 163
TIMELINE_TASK_ALIYUN_CMDB = 164
TIMELINE_TASK_CMDB_ALIYUN = 165
TIMELINE_TASK_VMWARE_CMDB = 166
TIMELINE_TASK_STATISTICS = 167
TIMELINE_TASK_DNS_FLUSH = 168
# SAFE WORK
TIMELINE_SAFEWORK_CREATE = 170
TIMELINE_SAFEWORK_STATUS = 171

# CONSOLE TRUCK
TIMELINE_CONSOLE_TRUCK_CREATE = 180
TIMELINE_CONSOLE_ENGINE_CREATE = 181
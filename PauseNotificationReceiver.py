# Copyright (c) 2022 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

from cloudvision.cvlib import ActionFailed
import requests
import json
import time
import uuid

state = ctx.action.args.get("state")
token = ctx.action.args.get("token")
switch = ctx.getDevice()
workspaceID = str(uuid.uuid4())
deviceId = (str(ctx.getDevice().id))
baseURL = 'https://www.cv-staging.corp.arista.io/'

headers = {"Authorization": "Bearer " + token, "Accept": "application/json"}

if state == 'yes':
    ctx.alog(f"State is yes")
    ctx.alog(str(ctx.getDevice().id))
    reply1 = requests.post(baseURL + 'api/resources/workspace/v1/WorkspaceConfig', data = '{"key":{"workspace_id":"%s"},"display_name":"assignMaintTag","description":"assignMaintTag"}'%(workspaceID), headers=headers)
    ctx.info(json.dumps(reply1.json()))
    reply2 = requests.post(baseURL + 'api/resources/tag/v2/TagConfig', data = '{"key":{"workspace_id":"%s", "element_type": "ELEMENT_TYPE_DEVICE", "label":"maint", "value":"yes"}}'%(workspaceID), headers = headers)
    ctx.info(json.dumps(reply2.json()))
    reply3 = requests.post(baseURL + 'api/resources/tag/v2/TagAssignmentConfig', data = '{"key": {"workspace_id": "%s", "elementType": "ELEMENT_TYPE_DEVICE", "label": "maint", "value": "yes", "deviceId": "%s" }, "remove": false}'%(workspaceID, deviceId), headers=headers)
    ctx.info(json.dumps(reply3.json()))
    reply4 = requests.post(baseURL + 'api/resources/workspace/v1/WorkspaceConfig', data = '{"key":{"workspace_id":"%s"},"request":"REQUEST_START_BUILD","request_params":{"request_id":"assignMaintTag"}}'%(workspaceID), headers = headers)
    ctx.info(json.dumps(reply4.json()))
    time.sleep(30)
    reply5 = requests.post(baseURL + 'api/resources/workspace/v1/WorkspaceConfig', data = '{"key":{"workspace_id":"%s"},"request":"REQUEST_SUBMIT","request_params":{"request_id":"assignMaintTag2"}}'%(workspaceID), headers = headers)
    ctx.info(json.dumps(reply5.json()))
elif state == 'no':
    ctx.alog(f"State is no")
    ctx.alog(str(ctx.getDevice().id))
    reply1 = requests.post(baseURL + 'api/resources/workspace/v1/WorkspaceConfig', data = '{"key":{"workspace_id":"%s"},"display_name":"deleteMaintTag","description":"deleteMaintTag"}'%(workspaceID), headers=headers)
    ctx.info(json.dumps(reply1.json()))
    reply2 = requests.post(baseURL + 'api/resources/tag/v2/TagAssignmentConfig', data = '{"key": {"workspace_id": "%s", "elementType": "ELEMENT_TYPE_DEVICE", "label": "maint", "value": "yes", "deviceId": "%s" }, "remove": true}'%(workspaceID, deviceId), headers = headers)
    ctx.info(json.dumps(reply2.json()))
    reply3 = requests.post(baseURL + 'api/resources/workspace/v1/WorkspaceConfig', data = '{"key":{"workspace_id":"%s"},"request":"REQUEST_START_BUILD","request_params":{"request_id":"deleteMaintTag"}}'%(workspaceID), headers = headers)
    ctx.info(json.dumps(reply3.json()))
    time.sleep(30)
    reply4 = requests.post(baseURL + 'api/resources/workspace/v1/WorkspaceConfig', data = '{"key":{"workspace_id":"%s"},"request":"REQUEST_SUBMIT","request_params":{"request_id":"deleteMaintTag2"}}'%(workspaceID), headers = headers)
    ctx.info(json.dumps(reply4.json()))
else:
    raise ActionFailed((f"Invalid state (should be yes/no)"))

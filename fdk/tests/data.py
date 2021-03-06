# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import io
import ujson


json_request_without_body = {
    "call_id": "01C7Y3PZFM67WG200000000000",
    "deadline": "2018-03-06T18:54:32.788+02:00",
    "body": "",
    "content_type": "",
    "protocol": {
        "type": "http",
        "method": "GET",
        "request_url": "http://localhost:8080/r/test/new-python",
        "headers": {
            "Accept": ["*/*", ],
            "User-Agent": ["curl/7.54.0"],
        }
    }
}

cloudevent_request_without_body = {
    "cloudEventsVersion": "0.1",
    "eventID": "01C7Y3PZFM67WG200000000000",
    "source": "fdk-python",
    "eventType": "fdk-cloudevent-test",
    "eventTypeVersion": "0.1",
    "eventTime": "2018-03-06T18:54:32.788+02:00",
    "schemaURL": "...",
    "contentType": "application/json",
    "extensions": {
        "deadline": "2018-03-06T18:54:32.788+02:00",
        "protocol": {
            "type": "http",
            "method": "GET",
            "request_url": "http://localhost:8080/r/myapp/myfunc?q=hi",
            "headers": {
                "Accept": ["*/*", ],
                "User-Agent": ["curl/7.54.0"],
            }
        }
    },
    "data": {}
}


json_request_with_body = {
    "call_id": "01C7Y3PZFM67WG200000000000",
    "deadline": "2018-03-06T18:54:32.788+02:00",
    "body": '{"name": "John"}',
    "content_type": "",
    "protocol": {
        "type": "http",
        "method": "POST",
        "request_url": "http://localhost:8080/r/test/new-python",
        "headers": {
            "Accept": ["*/*", ],
            "User-Agent": ["curl/7.54.0"],
        }
    }
}


cloudevent_request_with_body = {
    "cloudEventsVersion": "0.1",
    "eventID": "01C7Y3PZFM67WG200000000000",
    "source": "fdk-python",
    "eventType": "fdk-cloudevent-test",
    "eventTypeVersion": "0.1",
    "eventTime": "2018-03-06T18:54:32.788+02:00",
    "schemaURL": "...",
    "contentType": "application/json",
    "extensions": {
        "deadline": "2018-03-06T18:54:32.788+02:00",
        "protocol": {
            "type": "http",
            "method": "GET",
            "request_url": "http://localhost:8080/r/myapp/myfunc?q=hi",
            "headers": {
                "Accept": ["*/*", ],
                "User-Agent": ["curl/7.54.0"],
            }
        }
    },
    "data": '{"name": "John"}'
}


def to_stream(dct):
    return io.BytesIO(
        ujson.dumps(dct).encode("utf-8"))

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

import dill
import fdk
import sys
import ujson

from fdk import response


def handler(context, data=None):
    """
    General purpose Python3 function processor

    Why general purpose?

     - It supports any call from Fn-powered Python applications
       that utilizes corresponding API to run
       distributed Python functions

    How is it different from other Python FDK functions?

     - This function works with serialized Python callable objects via wire.
       Each function supplied with set of external dependencies that are
       represented as serialized functions, no matter if they are module-level,
       class-level Python objects

    :param context: request context
    :type context: fdk.context.RequestContext
    :param data: request data
    :type data: dict
    :return: resulting object of distributed function
    :rtype: object
    """
    payload = ujson.loads(data)
    (self_in_bytes,
     action_in_bytes, action_args, action_kwargs) = (
        payload['self'],
        payload['action'],
        payload['args'],
        payload['kwargs'])

    print("Got {} bytes of class instance".format(len(self_in_bytes)),
          file=sys.stderr, flush=True)
    print("Got {} bytes of function".format(len(action_in_bytes)),
          file=sys.stderr, flush=True)

    print("string class instance unpickling",
          file=sys.stderr, flush=True)
    self = dill.loads(bytes(self_in_bytes))
    print("class instance unpickled, type: ", type(self),
          file=sys.stderr, flush=True)
    print("string class instance function unpickling",
          file=sys.stderr, flush=True)
    action = dill.loads(bytes(action_in_bytes))
    print("class instance function unpickled, type: ",
          type(action), file=sys.stderr, flush=True)

    action_args.insert(0, self)

    dependencies = action_kwargs.get("dependencies", {})
    print("cached external methods found: ", len(dependencies) > 0,
          file=sys.stderr, flush=True)
    for name, method_in_bytes in dependencies.items():
        dependencies[name] = dill.loads(bytes(method_in_bytes))

    action_kwargs["dependencies"] = dependencies

    print("cached dependencies unpickled", file=sys.stderr, flush=True)

    try:
        res = action(*action_args, **action_kwargs)
    except Exception as ex:
        print("call failed", file=sys.stderr, flush=True)
        return response.RawResponse(
            context,
            status_code=500,
            response_data=str(ex))

    print("call result: {}".format(res), file=sys.stderr, flush=True)

    return response.RawResponse(
        context,
        status_code=200,
        response_data=res)


if __name__ == "__main__":
    fdk.handle(handler)

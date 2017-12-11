"""
Copyright 2017 NREL

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
"""

class BaseObject(object):
    """
        The BaseObject class is the basis for all other classes.

        valid(self) -> bool
            checks object validity based on null attributes
    """

    def __init__(self):
        self.placeholder = "this is a placeholder for future use"

    def valid(self):
        valid = True

        selfvalues = self.__dict__.values()
        if None in selfvalues:
            valid = False
            print("in ", self)
            for key in self.__dict__.keys():
                if self.__dict__[key] == None:
                    print(key + " has value None")

        return valid
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Directories where static content files used by Cobalt are located.
{
  'variables': {
    'static_contents_source_dir': '<(DEPTH)/cobalt/content',
    'static_contents_output_base_dir': '<(PRODUCT_DIR)/content',
    'static_contents_output_data_dir': '<(PRODUCT_DIR)/content/data',
  },
}
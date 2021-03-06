# Copyright {{ cookiecutter.year }} {{ cookiecutter.full_name }}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "{{ cookiecutter.project_name }}"
__summary__ = "{{ cookiecutter.project_short_description }}"
__uri__ = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"

__version__ = "{{ cookiecutter.version }}"

__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"

__license__ = "Apache License, Version 2.0"
__copyright__ = "Copyright {{ cookiecutter.year }} %s" % __author__

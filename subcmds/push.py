# Copyright (C) 2008 The Android Open Source Project
# Copyright (C) 2017 Wave Computing, Inc.  John McGehee
# Copyright (C) 2022 Known Rabbit
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from hooks import RepoHook
from subcmds.upload import Upload


class Push(Upload):
  COMMON = True
  GERRIT = False
  helpSummary = "Push changes to remote"
  helpUsage = """
%prog [--re --cc] [<project>]...
"""
  helpDescription = """

The '%prog' command sends changes to the central repository, such as GitHub or
GitLab.  Alternatively, use the 'upload' command to send changes to the Gerrit
Code Review system.

'%prog' searches for topic branches in local projects that have not yet been
pushed.  If multiple topic branches are found, '%prog' opens an editor to allow
the user to select which branches to push.

'%prog' searches for changes ready to be pushed in all projects listed on the
command line.  Projects may be specified either by name, or by a relative or
absolute path to the project's local directory. If no projects are specified,
'%prog' will search for changes in all projects listed in the manifest.
"""

  def _Options(self, p):
    p.add_option('--br', '--branch',
                 type='string', action='store', dest='branch',
                 help='(local) branch to upload')
    p.add_option('-c', '--current-branch',
                 dest='current_branch', action='store_true',
                 help='upload current git branch')
    p.add_option('-o', '--push-option',
                 type='string', action='append', dest='push_options',
                 default=[],
                 help='additional push options to transmit')
    p.add_option('-D', '--destination', '--dest',
                 type='string', action='store', dest='dest_branch',
                 metavar='BRANCH',
                 help='Push to this target branch on the remote.')
    p.add_option('-n', '--dry-run',
                 dest='dryrun', default=False, action='store_true',
                 help='do everything except actually upload the CL')
    RepoHook.AddOptionGroup(p, 'pre-upload')

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
    p.add_option('-D', '--destination', '--dest',
                 type='string', action='store', dest='dest_branch',
                 metavar='BRANCH',
                 help='Push to this target branch on the remote.')
    p.add_option('-n', '--dry-run',
                 dest='dryrun', default=False, action='store_true',
                 help='do everything except actually upload the CL')

    # Options relating to upload hook.  Note that verify and no-verify are NOT
    # opposites of each other, which is why they store to different locations.
    # We are using them to match 'git commit' syntax.
    #
    # Combinations:
    # - no-verify=False, verify=False (DEFAULT):
    #   If stdout is a tty, can prompt about running upload hooks if needed.
    #   If user denies running hooks, the upload is cancelled.  If stdout is
    #   not a tty and we would need to prompt about upload hooks, upload is
    #   cancelled.
    # - no-verify=False, verify=True:
    #   Always run upload hooks with no prompt.
    # - no-verify=True, verify=False:
    #   Never run upload hooks, but upload anyway (AKA bypass hooks).
    # - no-verify=True, verify=True:
    #   Invalid
    p.add_option('--no-cert-checks',
                 dest='validate_certs', action='store_false', default=True,
                 help='Disable verifying ssl certs (unsafe).')
    p.add_option('--no-verify',
                 dest='bypass_hooks', action='store_true',
                 help='Do not run the push hook.')
    p.add_option('--verify',
                 dest='allow_all_hooks', action='store_true',
                 help='Run the push hook without prompting.')


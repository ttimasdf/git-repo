# repo

Repo is a tool built on top of Git.  Repo helps manage many Git repositories,
does the uploads to revision control systems, and automates parts of the
development workflow.  Repo is not meant to replace Git, only to make it
easier to work with Git.  The repo command is an executable Python script
that you can put anywhere in your path.

This fork was enhanced to add:
1. A `repo push` command that performs an ordinary push of the topic branch on all repositories.  This allows you to
   push the topic branches to GitHub or GitLab, where you can create a pull request or merge request and get your code
   reviewed.  The existing `repo upload` command continues to upload to Gerrit as usual.
2. All operations are executed in the same order as defined in the manifest file.  In particular, `repo push` and
   `repo upload` push to the repositories in the same order that the ``<project>`` elements appear in the manifest file.

* Homepage: <https://gerrit.googlesource.com/git-repo/>
* Mailing list: [repo-discuss on Google Groups][repo-discuss]
* Bug reports: <https://bugs.chromium.org/p/gerrit/issues/list?q=component:repo>
* Source: <https://gerrit.googlesource.com/git-repo/>
* Overview: <https://source.android.com/source/developing.html>
* Docs: <https://source.android.com/source/using-repo.html>
* [repo Manifest Format](./docs/manifest-format.md)
* [repo Hooks](./docs/repo-hooks.md)
* [Submitting patches](./SUBMITTING_PATCHES.md)
* Running Repo in [Microsoft Windows](./docs/windows.md)
* GitHub mirror: <https://github.com/GerritCodeReview/git-repo>
* Postsubmit tests: <https://github.com/GerritCodeReview/git-repo/actions>

## Contact

Please use the [repo-discuss] mailing list or [issue tracker] for questions.

You can [file a new bug report][new-bug] under the "repo" component.

Please do not e-mail individual developers for support.
They do not have the bandwidth for it, and often times questions have already
been asked on [repo-discuss] or bugs posted to the [issue tracker].
So please search those sites first.

## Install

Many distros include repo, so you might be able to install from there.
```sh
# Debian/Ubuntu.
$ sudo apt-get install repo

# Gentoo.
$ sudo emerge dev-vcs/repo
```

You can install it manually as well as it's a single script.
```sh
$ mkdir -p ~/.bin
$ PATH="${HOME}/.bin:${PATH}"
$ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
$ chmod a+rx ~/.bin/repo
```


[new-bug]: https://bugs.chromium.org/p/gerrit/issues/entry?template=Repo+tool+issue
[issue tracker]: https://bugs.chromium.org/p/gerrit/issues/list?q=component:repo
[repo-discuss]: https://groups.google.com/forum/#!forum/repo-discuss

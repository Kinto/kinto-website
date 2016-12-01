# The Kinto website

This repository contains the code behind the Kinto website. It's powered by
[Pelican](http://www.getpelican.com), [Travis-CI](http://travis-ci.org/) and
Github pages.

## How to run locally

If you want to build the website locally, it's as simple as this:

```bash

  $ git clone https://github.com/Kinto/kinto-website.git
  $ cd kinto-website
  $ make install
  $ make regenerate
```

And head to [http://localhost:8000/](http://localhost:8000/).

## How to push updates to the online website

The repository is configured to trigger a build each time a commit hits the
*master* branch. As such, it means that you don't need to do anything else than
merging the pull requests, and the site should be built for you.

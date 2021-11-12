# cadquery on the Read The Docs.
translated docs for cadquery official document

:us:

[![Documentation Status](https://readthedocs.org/projects/cadquery/badge/?version=latest)](https://cadquery.readthedocs.io/en/latest/?badge=latest)

:jp:

[![Documentation Status](https://readthedocs.org/projects/cadquery-ja/badge/?version=latest)](https://cadquery-ja.readthedocs.io/ja/latest/?badge=latest)

This is a project to provide cadquery official documentation with multiple versions and multiple languages on Read The Docs site.

Current procedure is bit tricky because Read The Docs doesn't have a way to specify options for sphinx-build command.
conf.py files for each languages have 'language' and 'locale_dirs' values without having full copy of conf.py of sphinx doc. If we want to specify conf.py file that is out of source directory, we will use '-c' option for sphinx-build command. Unfortunately Read the Docs can't. If there are any better way, please let me know.

## URLs

* RTD project pages for Sphinx:

  * https://readthedocs.org/projects/cadquery/  (Master)
  * https://readthedocs.org/projects/cadquery-ja/

* Documentation pages for each languages:

  * https://cadquery.readthedocs.io/en/latest/
  * https://cadquery.readthedocs.io/ja/latest/

## How to setup a translated documentation project on RTD

Detail is here: https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Points are:

* We must have RTD projects for each languages.
* Each projects must have correct Language setting on "Settings" page.
* Master project has connections to each translated projects on "translations settings" page.


## How to update po files

```
sh ./locale/update.sh
```

After that, you should commit updated po files.


## How to add a language

1. add language to locale/update.sh:

   ```
   - rm -R ja
   - tx pull -l ja
   + rm -R ja de
   + tx pull -l ja,de
   ```

2. update po files

3. commit them

4. add new project on Read The Docs like:

   https://readthedocs.org/projects/cadquery-ja/

5. add translation project to parent project like:

   https://readthedocs.org/dashboard/cadquery/translations/

# -*- coding: utf-8 -*-
# vim: ft=sls

{## import settings from map.jinja ##}
{% from "sysstat/map.jinja" import sysstat_settings with context %}

sysstat-pkg:
  pkg.installed:
    - name: {{ sysstat_settings.pkg }}
    - failhard: True

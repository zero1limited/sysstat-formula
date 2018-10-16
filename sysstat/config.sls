# -*- coding: utf-8 -*-
# vim: ft=sls

{## import settings from map.jinja ##}
{% from "sysstat/map.jinja" import sysstat_settings with context %}
{% set config_settings = sysstat_settings.config %}

sysstat-default:
  file.managed:
    - name: {{ config_settings.default_path }}
    - source: salt://sysstat/files/sysstat.default
    - mode: 644
    - user: root
    - group: root
    - template: jinja
    - defaults:
        enabled: "{{ config_settings.enabled }}"
        sa1_options: {{ config_settings.sa1_options }}
        sa2_options: {{ config_settings.sa2_options }}
    {% if sysstat_settings.service.enabled %}
    - listen_in:
      - service: sysstat-service
    {% endif %}

sysstat-cron:
  file.managed:
    - name: {{ config_settings.cron_path }}
    - source: salt://sysstat/files/cron
    - mode: 644
    - user: root
    - group: root
    - template: jinja
    - defaults:
        schedule: {{ config_settings.schedule }}
    
sysstat-config:
  file.managed:
    - name: {{ config_settings.config_path }}
    - source: salt://sysstat/files/config
    - mode: 644
    - user: root
    - group: root
    - template: jinja
    - defaults:
        history: {{ config_settings.history }}
        compressafter: {{ config_settings.compressafter }}


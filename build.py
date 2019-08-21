#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder()
    builder.add(settings={"arch": "x86_64", "build_type": "Release"},
                options={}, env_vars={}, build_requires={})
    builder.run()

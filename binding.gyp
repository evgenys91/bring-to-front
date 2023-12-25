{
  "targets": [
    {
      "target_name": "bringToFront",
      'sources': [
        "src/index.cc"
      ],
      'conditions': [
        ['OS=="win"', {'sources': [
          "<(module_root_dir)/src/win32/pidToFront.cc"
        ]}],
        ['OS=="mac"', {
          'cflags': ['-fvisibility=hidden'],
          'xcode_settings': {}
        }],
        ['OS=="linux"', {}]
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "libraries": [
      ]
    }
  ]
}
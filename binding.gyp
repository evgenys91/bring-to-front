{
  "targets": [
    {
      "target_name": "bringToFront",
      'sources': [],
      'conditions': [
        ['OS=="win"', {'sources': [
          "src/index.cc",
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
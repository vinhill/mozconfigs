# Mozconfig manager

Just the setup that emilio came up with to manage his builds.

## Usage

Just put the `bin` directory somewhere in your `PATH` and do:

```
$ buildwith debug
```

For a debug build, or:

```
$ buildwith debug asan noopt
```

For an unoptimized asan build. And so on.

## Common configs

- debug noopt-dom
- debug noopt-dom android-emulator
- opt

## Configuration

Put checked-in modifiers into `mozconfigs/` and local ones into `user-configs/`.
If the same modifier exists in both places, `user-configs/` wins.

Add a `buildwith.conf` to define which modifiers are always included:

```bash
DEFAULT_MODIFIERS+=(
  buildcache
  sccache
)
```

Those default modifiers are included in the generated mozconfig, but are not
part of the identifier or object directory name.

Git repo: https://github.com/emilio/mozconfigs

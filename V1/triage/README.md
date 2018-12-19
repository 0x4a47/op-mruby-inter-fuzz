# Tech

Using [crash walk](https://github.com/bnagy/crashwalk) to triage

Will implement [COV](https://github.com/mrash/afl-cov) 

# Commands

> We have to ensure that the binary we are fuzzing is in the PATH.

I have added mruby to `/opt` which I have made a directory checked in the path, so just put all binaries we are fuzzing in here.
Also, call `afl-fuzz` from the `HOME` directory as it helps with the `cwtriage` tool.

eg:

```
$ cd ~ 
$ afl-fuzz -i ~/tools/testcases/ruby-corpus-light/mruby-testcases/ -x ~/other-stuff/dictionaries/ruby-keywords.dict -o ~/afl-outdirectories/mruby-29-5-17-1 -- mruby @@
```

Also the `--` is needed otherwise `cwtriage` shits the bed.

The command we call to triage is then:

```
$ cwtriage -root ~/afl-outdirectories/mruby-29-5-17-1/ -afl -tidy
```

Which analyzes everything in the `root` argument, and moves all crash cases that do *NOT* crash within the gdb emulation in `<blah>/crashes/.cwtidy` so if we need them, that's where they are.

This is done such that when the cwtriage command is called again then these cases aren't analyzed again (waste of time).

To get the triage output:

```
$ cwdump crashwalk.db > triage.txt
```

Which will dump *ALL* the crashes stored in `crashwalk.db` to the output file.

Will look into a way to find new crashes and let us know of these - although could probably do with `cwfind`.

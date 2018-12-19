# op-inter-fuzz
storage for thoughts, notes, etc.

# compiling

afl-covcompile:
```
CFLAGS="-fprofile-arcs -ftest-coverage" ./minirake
```

afl-asan:
```
root@afl-fuzz-asan:~/ibb/mruby# CFLAGS="-O1 -g -fsanitize=address -fno-omit-frame-pointer"  LDFLAGS="-g -fsanitize=address" ./minirake
```
or:
```
root@afl-fuzz-asan:~/ibb/mruby# AFL_USE_ASAN=1 ./minirake
```

when using asan during fuzzing please have `export ASAN_OPTIONS='abort_on_error=1'` so the binary actually crashes during runtime and afl knows its a bug


## Information Resources
- [Awesome Fuzzing Resource Repo](https://github.com/secfigo/Awesome-Fuzzing/blob/master/README.md)
- [Rust Regex fuzzing with libfuzz](https://www.nibor.org/blog/fuzzing-is-magic---or-how-i-found-a-panic-in-rusts-regex-library/)
- [Fuzzing python with AFL](https://alexgaynor.net/2015/apr/13/introduction-to-fuzzing-in-python-with-afl/)
- [Python+afl = pyjfuzz](https://www.dzonerzy.net/post/pyjfuzz-to-the-next-level)
- [Python+afl = pyjfuzz 2](https://www.dzonerzy.net/post/a-bit-bout-fuzzing)
- [interpreter bugs](https://github.com/dyjakan/interpreter-bugs)
- [Sean Heelan's fuzzing work](https://sean.heelan.io/2016/04/26/fuzzing-language-interpreters-using-regression-tests/)
- [Ben Nagy's fuzzing work](https://github.com/bnagy/slides/blob/master/fuzzing_without_pub.pdf)
- [Geeknik's fuzzing work](http://www.geeknik.net/71nvhf1fp)
- [Emmanuel Law fuzzing PHP talk](https://www.youtube.com/watch?v=I29FEZn1pw4&t=1704s)

## tutorials, walkthroughs etc
- [Libfuzzer via google](https://github.com/google/fuzzer-test-suite/blob/master/tutorial/libFuzzerTutorial.md)
- [Libfuzzer workshop](https://github.com/Dor1s/libfuzzer-workshop/)
- [Fuzz from start --> finish](https://foxglovesecurity.com/2016/03/15/fuzzing-workflows-a-fuzz-job-from-start-to-finish/)

## Project idea's.
- Fuzzing ruby interpreter directly.
  - Requires a syntactically (grammatically) correct mutation algorithm.
  - potentially use regression testing to generate new test cases
  - Seems hard to do without reinventing the wheel or maybe looking at prior projects such as Phzzer (Emmanuel law's php fuzzer).

  ### V0.1
    -[afl-fuzz -x 1](https://lcamtuf.blogspot.com.au/2015/04/finding-bugs-in-sqlite-easy-way.html)
    -[afl-fuzz -x 2](https://lcamtuf.blogspot.com.au/2015/01/afl-fuzz-making-up-grammar-with.html)
    - Currently fuzzing mruby using a .dict file created for afl fuzz.
    - This allows afl to find and identify the user tokens we supplied and mutate the testcases with those tokens.
    - the command we are running with is as follows:
      `screen afl-fuzz -i test/ -x ruby-keywords.dict -o out_dir ../ibb/mruby/bin/mruby`
    - where -x is our dict file.
    - In the afl-fuzz-1 box, we have 1 crash and 9 hangs @ 11:00 on the 29th of May. Crash is a false positive.
    - compiled with:
      > CFLAGS="-O1 -g -fsanitize=address -fno-omit-frame-pointer"  LDFLAGS="-g -fsanitize=address" ./minirake

- Fuzzing functions WITHIN ruby itself.
  - Break the regex parser ?
  - Break anything that parses stuff
  - Main idea is that we want to generate test cases and mutate bytes within a .rb file, this will then allow us to pass data to the raw ruby function instead of mutating and parsing the whole file to the interpreter, we can focus on one function.
  - See [Rust Regex fuzzing with libfuzz], the idea is similar except using AFL & in ruby not rust.
  - seems simpler because of the following inbuilt ruby options:
    -[Running C in Ruby](http://silverhammermba.github.io/emberb/embed/)
    -[Running Ruby in C](http://silverhammermba.github.io/emberb/embed/)
    - See current.jpg & aim.jpg for potential setup.
  - Maybe use Frida for coverage ? [Frida](https://www.frida.re/)  
  - Make use of Ruby's Exception handlers to track results ? [Exception Tree](http://blog.nicksieger.com/articles/2006/09/06/rubys-exception-hierarchy/)    
  - Do we need to think about CPU Cycles & exec/s

## Other links
 - [Quickfuzz](https://github.com/CIFASIS/QuickFuzz)  
 - [ffi](https://www.amberbit.com/blog/2014/6/12/calling-c-cpp-from-ruby/)
 - [ffi 2](https://github.com/ffi/ffi/wiki/Core-Concepts)

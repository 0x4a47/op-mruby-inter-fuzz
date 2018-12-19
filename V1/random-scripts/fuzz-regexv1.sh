#!/usr/bin/env ruby
#puts "<<<fuzzng ruby regex>>>"
a = gets.chomp
begin
    x = Regexp.new(a)
rescue StandardError=>e
    puts ">>>error occurred<<<"
    puts e
else
    puts "<<<parsed correctly>>>"
    puts x
end

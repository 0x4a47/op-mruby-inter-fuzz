# op-inter-fuzz
This was a brief project that myself and @glem had a go at. We learn't heaps however, didn't have much success. The reasons behind why I believe our success was limited was 2 fold: 
1. We weren't using a targeted enough approach, fuzzing interpreters from the top-down requires either a really good custom language-aware fuzzer OR, a hell of alot of cores. We didn't have either and therefore didn't have a huge amount of success. 
2. We didn't take a step back and realise what we were doing wrong or, what we could've done better. This was mainly because this project was a harness for having a crack at fuzzing some stuff. Mistakes are a good way to learn :) 

Nothing you'll see in this github repo is 'new' however, the idea would be that someone might stumble across this one-day and take what we did, what others did, what they did, and put it to good use. The same can be said for the ideas in the next section. We wanted to do a 'Version 2' however, time was limited and nothing ever came of it. Again, these ideas are not new, just a braindump that someone, somewhere, might find useful :) 

---------------------------------------------------------------------------------------------------------
# V2
This is our second attempt at fuzzing 4 profit. Our last was fun and informative using AFL for mruby interpreter fuzzing however we only seemed to find recursive overflows which != profit. This time, we are looking into fuzzing Image library / renderers in browsers. This is a much easier route to begin with and pure mutational algorithms can bring us success if we can get a decent target. For the old Readme and other items see V1 Folder.

# New Ideas
 - Browser fuzzing
 - Image Library / renderer fuzzing
 - PDF Reader / Viewer Fuzzing
 - Games? (0x4a47 thinks this would be fun but hard)
 - Antivirus was mentioned but i think aforementioned targets are +1

# Targets for Browser / Image renderer fuzzing
 - Waterfox
 - Firefox (No sandbox)
 - Safari (Blackbox so slow and hard)
 - Chrome (4 the hardcorez)
 - Opera ? (lol)

# Browser Fuzzing Links / Resources
 - [Brown Renderer fuzzing](http://2015.zeronights.org/assets/files/16-Brown.pdf)
 - [Browser Fuzzing in 2014](https://www.syscan360.org/slides/2014_EN_BrowserFuzzing_RosarioValotta.pdf)
 - [Some wierd vietnamese thing](https://www.mindomo.com/mindmap/browser-fuzzing-4ae6c56541644ab3981c0b71ddf5c818)
 - [Fuzz testing of Web Browsers](https://ucaat.etsi.org/2015/presentations/HTB_HODOVAN.pdf)
 - [Browser fuzzing in 2014 v2?](https://conference.hitb.org/hitbsecconf2014kul/materials/D2T2%20-%20Rosario%20Valotta%20-%20Browser%20Fuzzing%20in%202014.pdf)
 

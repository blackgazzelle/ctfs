TF: Cyberstakes 2020
Challenge: Reverse Engineering 101

Category:  RE

Points: 20

Difficulty: Introductory

## Instructions

***Description:***

Reverse engineering can definitely be intimidating so we have a simple program
with which you can start. If you don't know where to start, check out the hints
where well walk you through two different ways to solve this
[problem](RE101).

***Hints:***

***Static analysis***: Static analysis is a process for examining a program
without having a computer execute any code.

- From a command line on Linux, executing `objdump -d RE101` will display the
assembly code for the executable sections of the program
(assumes you downloaded the file to the same folder).
- Flow of this program starts at \_start and proceeds 'down' the code.
- `objdump -t RE101` will print all of the 'symbols' in the program. These are
human-readable names for specific spots in memory. Symbols in the '.text
' section tend to be function names and symbols in '.bss', '.data', and
'.rodata' tend to be variable names.
- You should be able to see that the address of the 'flag' symbol (second
command) appears in the first instruction of the start(first command).
- The hex values that are moved look like they are in the printable ASCII range.

***Dynamic analysis***: Dynamic analysis is a method of examining
the program as it is running to learn more about what it does. A common
tool to help with this is a "debugger" like gdb.

1. `gdb RE101` will launch GDB and prepare it to debug our target, the RE101
executable. You may need to change the permissions on the downloaded file in
order to make it executable (`chmod a+x RE101`).
2. `break exit` will add a "breakpoint" which will pause
the program's execution when we reach this point in the code. We're able to
use '_exit' here as a convenience and could have also specified a memory
address instead.
3. `run` will start execution and keep running until we hit the breakpoint
we specified above.
4. `x /s &flag` tells GDB to "examine" a "string" located at the address of the
'flag' symbol ('&' is the C symbol for 'address of').

Instead of the dynamic analysis above, we could have also continued our static
analysis by studying the assembly code we produced earlier. In particular, we
can observe that the code is moving a pointer to the 'flag' variable into the
EDI register in the first line. It then 'moves' a series of byte-constants into
the memory location to which EDI points, 'incrementing' EDI in between each
move. The final three lines in '_exit' execute a Linux system call to 'exit',
but that is relevant for this problem.When doing reverse engineering of x86 and
x86-64 programs, Intel's instruction set reference can be very helpful. It can
be intimidating to look at, but looking up the assembly instruction in this
document will tell you exactly what it does.

## Solution

First I used `file` to check the kind of file it is, which showed it was a 32
bit ELF file. So I opened it in radare `r2 RE101` and ran aaa to analyze it,
then did v to enter visual mode. So what we can actually see is that the
entry0 function which is the only function that does work moves a series of
hex characters. The characters follow as:

0x41, 0x43, 0x49, 0x7b, 0x61, 0x5f, 0x62, 0x79, 0x74, 0x5f, 0x61, 0x74, 0x5f,
0x61, 0x61, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x7d

Which to me looks like all ascii printable characters, also I know
41 and 43 is A and C so it looks like it is the start to the flag and in fact
it does give the flag.

## Flag

`ACI{a_byte_at_a_time}`

## Mitigation

The security problem here is that there is special encryption done on the binary
to make analysis harder. The best way to mitigate this is to write code that
obfuscates your process or to obfuscate the binary itself.
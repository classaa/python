#!/usr/bin/expect -f

spawn chsh
expect -re "\\\[(.*)]:" {
	set value = $expect_out(1,string)
}
if { $value != "/bin/bash" } {
	send "/bin/bsah\r"
}
expect {
	"not exist." { puts "err" }
	"changed." {puts "ok" }
}

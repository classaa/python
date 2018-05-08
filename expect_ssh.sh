#!/usr/bin/expect -f

set user [lindex argv 0]
set password [ lindex argv 1]
set ip [lindex argv 2]
spwan ssh $user@$ip
expect {
  "yes/no"  { send "yes\r";exp_continue }
  "password" { send "$password\r" }
}
interact
expect eof

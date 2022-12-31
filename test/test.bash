#!/bin/bash

# SPDX-fileCopyrightText: 2022 Takumi Fukazawa
# SPDX-License-Identifier: BSD-3-Clause

ng ( ) {
       echo NG at Line $1
              res=1
      }
      res=0

      ### I/O TEST ###
       in=$(ros2 run mypkg listener)
      out=$(echo hi | ros2 run mypkg talker)
      [ "${in}" = "[INFO] [1672446416.922124800] [listener]: Listen: person_msgs.msg.Person(message='hi', log=1)" ] || ng ${LINENO}

       in=$(ros2 run mypkg listener)
      out=$(echo やあ！ | ros2 run mypkg talker )  
      [ "${in}" = "[INFO] [1672446457.499800800] [listener]: Listen: person_msgs.msg.Person(message='やあ！', log=1)" ] || ng ${LINENO}

       in=$(ros2 run mypkg listener)
      out=$(echo 2 | ros2 run mypkg talker) 
      [ "${in}" ="[INFO] [1672446473.421415400] [listener]: Listen: person_msgs.msg.Person(message='2', log=1)" ] || ng ${LINENO}

       in=$(ros2 run mypkg listener)
      out=$( echo  | ros2 run mypkg talker)
      [ "${in}" = "echo  | ros2 run mypkg talker" ] || ng ${LINENO}

      [ "$res" = 0 ] && echo OK
        exit $res

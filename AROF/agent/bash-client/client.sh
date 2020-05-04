#!/bin/sh

header1="Content-Type:application/json"
header2="Accept:application/json"
hostname="$1"                           # set to "$1" to pass this as argument
port="$2"                               # similarly set to "$2" to pass this as 2nd arg

# function exec_post {
#         curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/0?enable=false"
#         curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/1?enable=false"
#         curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/2?enable=false"
#         curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/3?enable=false"
# }

function exec_post {

        curl --request POST \
        --url "http://${hostname}:${port}/arof" \
        --header ${header1} \
        --data '{
                "arof-pool": [
                        {
                                "id": 0,
                                "enabled": false,
                                "wavelength": 1
                        },
                        {
                                "id": 1,
                                "enabled": false,
                                "wavelength": 1
                        },
                        {
                                "id": 2,
                                "enabled": false,
                                "wavelength": 1
                        },
                        {
                                "id": 3,
                                "enabled": false,
                                "wavelength": 1
                        }
                ]
        }'
}


function exec_get {
        curl --request GET --url "http://${hostname}:${port}/arof"
}

function exec_put {

#         curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/0?enable=true"
#         curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/1?enable=true"
#         curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/2?enable=true"
#         curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/3?enable=true"
# }

        curl --request PUT \
        --url http://${hostname}:${port}/arof \
        --header ${header1} \
        --data '{
                "arof-pool": [
                        {
                                "arof-id": 0,
                                "enabled": true,
                                "wavelength": 2
                        },
                        {
                                "arof-id": 1,
                                "enabled": true,
                                "wavelength": 2
                        },
                        {
                                "arof-id": 2,
                                "enabled": true,
                                "wavelength": 2
                        },
                        {
                                "arof-id": 3,
                                "enabled": true,
                                "wavelength": 2
                        }

                ]
        }'
}

function exec_post_set {

        curl --request POST \
        --url http://${hostname}:${port}/arof \
        --header ${header1} \
        --data '{
                "arof-pool": [
                        {
                                "id": 0,
                                "enabled": true,
                                "wavelength": 2
                        },
                        {
                                "id": 1,
                                "enabled": true,
                                "wavelength": 2
                        },
                        {
                                "id": 2,
                                "enabled": true,
                                "wavelength": 2
                        },
                        {
                                "id": 3,
                                "enabled": true,
                                "wavelength": 2
                        }

                ]
        }'
}

# function exec_delete {
#         curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/0"
#         curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/1"
#         curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/2"
#         curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/3"
# }

function exec_delete {
        curl -X DELETE --header ${header2} "http://${hostname}:${port}/arof"
}

echo "ENSURE LASERS OFF"
exec_post
echo "ENABLE LASERS"
# exec_put
exec_post_set
echo "GET OPERATIONS ON LASERS"
exec_get
echo "DISABLE LASERS"
exec_delete
exec_get

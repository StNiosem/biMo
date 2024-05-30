// Standard
#include <stdio.h>
#include <stdlib.h>

// Network
#include <Network/Network.h>

// Variables
#define server = 'dj'
#define node = 'node.txt'


void GlobalServerHandler() {
    printf("ServerHandler");
    printf("this is probably not good");
    NDR_record_t(hServerId);
};
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <ctype.h>

#define MAX_PORT 65535

int port_scan(char *ip, int port)
{
    int sock, result;
    struct sockaddr_in addr;

    sock = socket(AF_INET, SOCK_STREAM, 0);

    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(ip);
    addr.sin_port = htons(port);

    result = connect(sock, (struct sockaddr *)&addr, sizeof(addr));

    close(sock);

    return result;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("[-] Not enough arguments\n");
        exit(1);
    }

    printf("Python Port Scanner\n");

    char *ip = argv[1];
    int open_ports[MAX_PORT];
    int count = 0;

    for (int port = 1; port <= MAX_PORT; port++)
    {
        printf("Scanning port %d\r", port);
        fflush(stdout);

        if (port_scan(ip, port) == 0)
        {
            printf("[+] Open %d\n", port);
            open_ports[count++] = port;
        }
    }

    printf("\n");

    if (count == 0)
    {
        printf("No open ports found.\n");
    }
    else
    {
        printf("Open ports: ");
        for (int i = 0; i < count; i++)
        {
            printf("%d ", open_ports[i]);
        }
        printf("\n");
    }

    return 0;
}

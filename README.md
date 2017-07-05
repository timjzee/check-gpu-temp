# check-gpu-temp

## Description
Checks GPU temperature during crypto currency mining, and stops the mining application if temperature exceeds a certain threshold. Mining application is assumed to be running in a detached Screen terminal. If multiple detached Screen terminals exist, the mining application is assumed to be running in the virtual terminal with the highest PID.

## Dependencies
- Python 3
- atitweak
- Screen

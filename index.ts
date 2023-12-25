
export function pid(pid: number): number {
    if (process.platform === 'win32') {
        const bringToFront = require('bindings')('bringToFront');
        return bringToFront.pidToFront(pid);
    }
    return -1;
}
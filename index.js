"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function pid(pid) {
    if (process.platform === 'win32') {
        const bringToFront = require('bindings')('bringToFront');
        return bringToFront.pidToFront(pid);
    }
    return -1;
}
exports.pid = pid;

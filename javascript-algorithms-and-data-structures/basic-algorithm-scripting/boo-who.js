function booWho(bool) {
    let type = typeof bool;

    if (type === 'boolean') {
        return true
    }

    return false
}

booWho(null);
/*
 * Browser storage methods
 * Requires Modernizr
 * v0.1
 * By Ernest Semerda
 * Semerda.com
 *
 */

SEMERDA.browserstorage = (function () {

    var support_obj = {
        localstorage   : false,
        sessionstorage : false,
        msg            : "Your browser dosent support local or session storage"
    }

    // show the keys currently held in the specified type of storage in the specified table
    function showStorageKeys(type, output_div) {
        // get the specified type of storage, i.e. local or session
        var storage = window[type + 'Storage'];
        if (storage.length > 0 && output_div.length > 0) {
            // remove the rows in the specified table before we start
            $(output_div + " > tbody > tr").remove();
        }
        else {
            $(output_div + " > tbody:last")
                .append("<tr><td>Nothing stored in browser storage.</td></tr>");
        }
        
        // loop through the existing keys in the storage and add them to the TBODY element as rows
        for (var i = 0; i < storage.length; i++) {
            var key = storage.key(i);
            var value = storage.getItem(key);
            console.log(key + ' = ' + value);

            if (output_div.length > 0) {
                $(output_div + " > tbody:last")
                .append("<tr><td>" + key + "</td>" +
                        "<td>" + value + "</td>" +
                        "<td><input type='submit' value='Remove' onclick='SEMERDA.browserstorage.remove(\"" + type + "\", \"" + key + "\");$(this).parent().parent().remove();'/></td></tr>");
            }
        }
    }

    function keyExists(type, key) {
        // get the specified type of storage, i.e. local or session
        var storage = window[type + 'Storage'];
        return (storage.getItem(key) === null ? false : true);
    }

    return {
        contains: function(key) {
            if (support_obj.localstorage) {
                return keyExists('local', key);
            } else if (support_obj.sessionstorage) {
                return keyExists('session', key);
            }
        },

        // adds a new key to both local and session storage
        set: function(key, value) {
            if (support_obj.localstorage) {
                localStorage.setItem(key, value);
            } else if (support_obj.sessionstorage) {
                sessionStorage.setItem(key, value);
            }
        },

        // removes an item with the specified key from the specified type of storage
        remove: function(type, key) {
            if (support_obj.localstorage) {
                localStorage.removeItem(key);
            } else if (support_obj.sessionstorage) {
                sessionStorage.removeItem(key);
            }
        },

        // show the keys currently held in the local and session storage
        get: function(key) {
            if (support_obj.localstorage) {
                return window['localStorage'].getItem(key);
            } else if (support_obj.sessionstorage) {
                return window['sessionStorage'].getItem(key);
            }
        },

        // show the keys currently held in the local and session storage
        showAll: function(output_div) {
            if (support_obj.localstorage) {
                showStorageKeys('local', output_div);
            } else if (support_obj.sessionstorage) {
                showStorageKeys('session', output_div);
            }
        },

        detect: function() {
            var supported = false;
            if (Modernizr.localstorage && Modernizr.sessionstorage) {
                support_obj = {
                    localstorage   : true,
                    sessionstorage : true,
                    msg            : "Your browser supports both local and session storage"
                }
                supported = true;
            } else {
                if (!Modernizr.localstorage) {
                    support_obj = {
                        sessionstorage : true,
                        msg            : "Your browser doesn't support local storage"
                    }
                } else {
                    support_obj = {
                        localstorage : true,
                        msg          : "Your browser doesn't support session storage"
                    }
                }
                supported = true;
            }
            return ({'supported' : supported, 'detail' : support_obj});
        },

        // clear all the held keys in the specified type of storage
        clearAll: function(type) {
            if (typeof type === 'undefined') {
                // Clear both local and session storage
                window['localStorage'].clear();
                window['sessionStorage'].clear();
            } 
            else {
               // get the specified type of storage, i.e. local or session
                var storage = window[type + 'Storage'];
                // clear the keys
                storage.clear();
            }
        }

    }

}());
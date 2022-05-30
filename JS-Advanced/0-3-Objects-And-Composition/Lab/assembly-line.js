function createAssemblyLine() {
    function hasClima(obj) {
        function adjustTemp() {
            if (this.temp > this.tempSettings) {
                this.temp--;
            } else if (this.temp < this.tempSettings) {
                this.temp++;
            }
        }

        const tmpObject = {
            'temp': 21,
            'tempSettings': 21,
            'adjustTemp': adjustTemp,
        };

        Object.assign(obj, tmpObject);
    }

    function hasAudio(obj) {
        function nowPlaying() {
            console.log(`Now playing '${this.currentTrack.name}' by ${this.currentTrack.artist}`);
        }

        const tmpObject = {
            'currentTrack': {
                'name': null,
                'artist': null,
            },
            'nowPlaying': nowPlaying
        };

        Object.assign(obj, tmpObject);
    }

    function hasParktronic(obj) {
        function checkDistance(distance) {
            let result = '';

            if (distance < 0.1) {
                result = 'Beep! Beep! Beep!';
            } else if (distance < 0.25) {
                result = 'Beep! Beep!';
            } else if (distance < 0.5) {
                result = 'Beep!';
            }

            console.log(result);
        }

        const tmpObject = {
            'checkDistance': checkDistance
        };

        Object.assign(obj, tmpObject);
    }

    return {
        'hasClima': hasClima,
        'hasAudio': hasAudio,
        'hasParktronic': hasParktronic,
    };
}


const assemblyLine = createAssemblyLine();

const myCar = {
    make: 'Toyota',
    model: 'Avensis'
};

assemblyLine.hasClima(myCar);
console.log(myCar.temp);
myCar.tempSettings = 18;
myCar.adjustTemp();
console.log(myCar.temp);
// Output
// 21
// 20


assemblyLine.hasAudio(myCar);
myCar.currentTrack = {
    name: 'Never Gonna Give You Up',
    artist: 'Rick Astley'
};
myCar.nowPlaying();
// Output
// Now playing 'Never Gonna Give You Up' by Rick Astley

assemblyLine.hasParktronic(myCar);
myCar.checkDistance(0.4);
myCar.checkDistance(0.2);
// Output
// Beep!
// Beep! Beep!

console.log(myCar);

// Output
// {
//     make: 'Toyota',
//         model: 'Avensis',
//     temp: 20,
//     tempSettings: 18,
//     adjustTemp: [Function],
//     currentTrack: {
//     name: 'Never Gonna Give You Up',
//         artist: 'Rick Astley'
// },
//     nowPlaying: [Function],
//         checkDistance: [Function]
// }

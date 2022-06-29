class SmartHike {
    constructor(username) {
        this.username = username;
        this.goals = {};
        this.listOfHikes = [];
        this._resources = 100;
    }

    get resources() {
        return this._resources;
    }

    set resources(value) {
        if (value > 100) {
            value = 100;
        }
        this._resources = value;
    }

    _canHike() {
        return this.resources > 0;
    }

    _getPeaksByCriteria(criteria) {
        return this.listOfHikes.filter(hike => hike.difficultyLevel === criteria);
    }

    addGoal(peak, altitude) {
        if (this.goals.hasOwnProperty(peak)) {
            return `${peak} has already been added to your goals`;
        }

        this.goals[peak] = altitude;
        return `You have successfully added a new goal - ${peak}`;
    }

    hike(peak, time, difficultyLevel) {
        if (!this.goals.hasOwnProperty(peak)) {
            throw new Error(`${peak} is not in your current goals`);
        }

        if (!this._canHike) {
            throw new Error(`You don't have enough resources to start the hike`);
        }

        if (this.resources - time * 10 < 0) {
            return 'You don\'t have enough resources to complete the hike';
        }

        this.resources -= time * 10;
        this.listOfHikes.push({
            peak,
            time,
            difficultyLevel
        });
        return `You hiked ${peak} peak for ${time} hours and you have ${this.resources}% resources left`
    }

    rest(time) {
        this.resources += time * 10

        if (this.resources === 100) {
            return `Your resources are fully recharged. Time for hiking!`;
        }

        return `You have rested for ${time} hours and gained ${time*10}% resources`;
    }

    showRecord(criteria) {
        if (this.listOfHikes.length === 0) {
            return `${this.username} has not done any hiking yet`;
        }

        if (criteria === 'all') {
            const message = ['All hiking records:'];
            const username = this.username;

            this.listOfHikes.forEach(function (hike) {
                message.push(`${username} hiked ${hike.peak} for ${hike.time} hours`)
            });

            return message.join('\n');
        }

        const peaks = this._getPeaksByCriteria(criteria);

        if (peaks.length === 0) {
            return `${this.username} has not done any ${criteria} hiking yet`;
        }

        const hike = peaks[0];
        return `${this.username}'s best ${criteria} hike is ${hike.peak} peak, for ${hike.time} hours`;
    }
}


// const user = new SmartHike('Vili');
// console.log(user.addGoal('Musala', 2925));
// console.log(user.addGoal('Rui', 1706));
// console.log(user.addGoal('Musala', 2925));


// const user = new SmartHike('Vili');
// console.log(user.addGoal('Musala', 2925));
// console.log(user.addGoal('Rui', 1706));
// console.log(user.hike('Musala', 8, 'hard'));
// console.log(user.hike('Rui', 3, 'easy'));
// console.log(user.hike('Everest', 12, 'hard'));


// const user = new SmartHike('Vili');
// console.log(user.addGoal('Musala', 2925));
// console.log(user.hike('Musala', 8, 'hard'));
// console.log(user.rest(4));
// console.log(user.rest(5));


// const user = new SmartHike('Vili');
// console.log(user.showRecord('all'));


// const user = new SmartHike('Vili');
// user.addGoal('Musala', 2925);
// user.hike('Musala', 8, 'hard');
// console.log(user.showRecord('easy'));
// user.addGoal('Vihren', 2914);
// user.hike('Vihren', 4, 'hard');
// console.log(user.showRecord('hard'));
// user.addGoal('Rui', 1706);
// user.hike('Rui', 3, 'easy');
// console.log(user.showRecord('all'));

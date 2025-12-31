import ClassRoom from "./0-classrom.js";

export default function initializeRooms() {
    const array = [19, 20, 34];
    const newArray = [];
    for (let element of array) {
        newArray.push(new ClassRoom(element));
    }
    return newArray
};

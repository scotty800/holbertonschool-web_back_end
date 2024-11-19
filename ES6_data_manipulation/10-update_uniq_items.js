export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterate through the map and update the quantity
  map.forEach((value, key) => {
    if (value === 1) {
      map.set(key, 100); // Update the quantity to 100
    }
  });

  return map;
}

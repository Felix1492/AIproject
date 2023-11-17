mod ecs;
use ecs::*;

fn main() {
    let mut world = World::new();

    // Add entities and systems to the world here
    // world.add_entity(...);
    // world.add_system(...);

    world.run_systems();
}
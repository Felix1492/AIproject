mod ecs;
use ecs::*;

mod model_inference;
use model_inference::*;

fn main() {
    let mut world = World::new();

    // Add entities and systems to the world here
    // world.add_entity(...);
    // world.add_system(...);

    // Load the model
    let model = Model::new("path/to/model.onnx").unwrap();

    // Run inference
    let input_data = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    let output_data = model.run_inference(&input_data).unwrap();

    world.run_systems();
}
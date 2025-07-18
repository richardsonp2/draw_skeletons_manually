# Microglia Skeleton Annotator

## Features 

- Load and display 2D images (TIFF, PNG, etc.)

- Manual drawing of skeleton structures using mouse input

- Save annotated skeletons to file

- [Planned] ML integration using image intensities as input (X) and skeletons as targets (y)

## Walkthrough

Clone the repository into a directive 

```bash
    git clone git@github.com:richardsonp2/draw_skeletons_manually.git
``` 

Run the script
```bash
python GUI_skeleton_draw.py
```

## TODO 
### Core Functionality

- Add Soma/Cell Body Drawing Tool

- For now: fixed-radius circle

- Later: freehand/multiline shape support

- Add GUI for selecting input/output paths

- Consider a pop-up dialog or file explorer
- Hotkeys for next cell, save skel, delete skel etc.

### Implement Drawing Tools

- Draw

- Erase

- Connect existing skeleton segments

### Image Handling

- Load image stacks

- Implement Max Intensity Projection (MIP) button

- Navigate slices (stack viewer)

### Machine Learning Integration

- Export X = image intensity vector (e.g., flattened pixel data)

- Export y = skeleton drawing as label

- Save as paired dataset file (e.g., .npz, .pkl, or custom format)

- Plan training/validation data structure, need automated pipeline. Perhaps even a server system to keep images?

💄 UI/UX Improvements

- Tool icons with visual feedback

- Colour selector for drawing

- Undo/Redo functionality

- Layer toggle (e.g., raw image vs annotations)

- Proper open and save icons


🤝 Contributing

This is a work in progress! Contributions are welcome—whether it's reporting bugs, suggesting features, or submitting pull requests.

Developed by Peter Richardson.
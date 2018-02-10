/*
 * Servo mounts for Leggett & Platt S-cape remote controller.
 *
 * All measurements are in mm. 
 * @author: Ouwen Huang <ouwen.oh@gmail.com>
 */
use <servo_clip_with_screws.scad>

// Constants
servo_holder_width = 10; 
servo_length = 34;
servo_offset = 4;

// Variable
base_width = 69;
base_thickness = 20;
remote_height = 20;
base_thickness_offset = 10;

module remote_holder(base_thickness_offset){
    union() {
        translate([0,0,-base_thickness+base_thickness_offset])cube([base_width,servo_length,base_thickness-base_thickness_offset]);
        translate([servo_holder_width,servo_offset,remote_height+base_thickness_offset])rotate([0,0,90])servo_clip();
        translate([base_width,servo_offset,remote_height+base_thickness_offset])rotate([0,0,90])servo_clip();
        cube([servo_holder_width,servo_length,remote_height+base_thickness_offset]);
        translate([base_width-servo_holder_width,0,0])cube([servo_holder_width,servo_length, remote_height+base_thickness_offset]);
    }
}

remote_holder(0);
translate([0,40,-base_thickness_offset])remote_holder(base_thickness_offset);
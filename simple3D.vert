attribute vec3 a_position;
attribute vec3 a_normal;

uniform mat4 u_model_matrix;
uniform mat4 u_view_matrix;
uniform mat4 u_projection_matrix;

uniform vec4 u_eye_position;

uniform vec4 u_light_position;
uniform vec4 u_light_diffuse;
uniform vec4 u_light_specular;
uniform vec4 u_light_ambiance;
uniform vec4 u_material_diffuse;
uniform vec4 u_material_specular;
uniform float u_material_shininess;

varying vec4 v_color;  //Leave the varying variables alone to begin with

void main(void)
{
	vec4 position = vec4(a_position.x, a_position.y, a_position.z, 1.0);
	vec4 normal = vec4(a_normal.x, a_normal.y, a_normal.z, 0.0);

	position = u_model_matrix * position;
	normal = normalize(u_model_matrix * normal);

	vec4 s = normalize(u_light_position - position);
	float lambert = max(dot(normal, s), 0);

	vec4 v = normalize(u_eye_position - position);
	vec4 h = normalize(s + v);
	float phong = max(dot(normal, h), 0);
	v_color = u_light_ambiance + u_light_diffuse * u_material_diffuse * lambert + u_light_specular * u_material_specular * pow(phong, u_material_shininess);

	position = u_view_matrix * position;
	position = u_projection_matrix * position;
	gl_Position = position;
}
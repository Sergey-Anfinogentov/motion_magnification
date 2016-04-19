;+
; :Description:
;    Generates random string
;
; :Params:
;    seed - Seed for a random sequence
;    length - length of the string to be generated
;
;
;
; :Author:  Sergey Anfinogentov (sergey.istp@gmail.com)
;-
function randomstring,seed,length
  common randomstring_common,s
  if not keyword_set(seed) then begin
    if keyword_set(s) then seed = s else $
      seed= systime(/sec)
  endif
  if n_params() eq 0 then begin
    s = seed
    length = 5
  endif
  if n_params() eq 1 then length=seed>1 else s=seed
  if not keyword_set(s) then s= systime(/sec)
  result = string(byte(97+25*randomu(s,length)))
  if n_params() eq 2 then seed=s
  return,result
end
;+
  ; :Description:
  ;    Reades 3D data cube from a binary file
  ;
  ; :Params:
  ;    file
  ;
  ;
  ;
  ; :Author:  Sergey Anfinogentov (sergey.istp@gmail.com)
  ;-
function load_cube,file
  openr,lun,file,/get_lun
  dim = lonarr(3)
  readu,lun,dim
  data = dblarr(dim[0],dim[1],dim[2])
  readu,lun,data
  close,lun
  free_lun,lun
  return,data
end

;+
  ; :Description:
  ;    Saves 3D data cube in a binary file
  ;
  ; :Params:
  ;    file
  ;    cube
  ;
  ;
  ;
  ; :Author:  Sergey Anfinogentov (sergey.istp@gmail.com)
  ;-
pro save_cube,file, cube
  openw,lun,file,/get_lun
  dim = long(size(cube,/dimensions))
  data = double(cube)
  writeu,lun,dim,data
  close,lun
  free_lun,lun
end
;+
; :Description:
;    This is a wraper for the motion magnification code written in Python.
;     The routine saves an input data cube in a temporary file and spawns the motion magnification programm.
;
; :Params:
;    input_cube - input data cube, dblarr(nx,ny,nt)
;    k - magnification factor
;    width - phase smoothing width
;
;
;
; :Author: Sergey Anfinogentov (sergey.istp@gmail.com)
;-
function magnify_2d, input_cube, k, width
  if not keyword_set(k) then k = 5.0
  if not keyword_set(width) then width = 30
  ;path to the magnify_cl.py
  py_pro = 'magnify_cl.py'
  ;Command to launch Python 3 interpretator
  python = 'python3'
  tmp_dir = GETENV('IDL_TMPDIR')
  rnd = randomstring()
  file_input = filepath(rnd+'.dat',root = tmp_dir)
  file_output = filepath(rnd+'.ampl.dat',root = tmp_dir)
  save_cube,file_input, input_cube
  cmd = python + ' "'+py_pro +'" "'+file_input+'" '+ strcompress(k,/remove_all) + ' ' + strcompress(width,/remove_all)
  spawn,cmd
  output_cube = load_cube(file_output)
  file_delete, [file_input, file_output]
  return, output_cube
end

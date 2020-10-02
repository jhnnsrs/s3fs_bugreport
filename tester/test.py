

import dask.array as da
import xarray
import s3fs
import xarray as xr

bucket = "zarr"
name = "sdfsefsef"

nana = xarray.DataArray(da.random.random((1024,1024,10,2,1)))



s3_path = f"{bucket}/{name}"
s3 = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "s3://minioserver:9000"}, username="weak_access_key", password="weak_secret_key")
s3store = s3.get_mapper(s3_path)


print("Storing")
nana.to_dataset().to_zarr(store=s3store, mode="w", consolidated=True, compute=True)
print("Getting")

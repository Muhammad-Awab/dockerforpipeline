FROM mcr.microsoft.com/dotnet/framework/runtime:4.8-windowsservercore-ltsc2019 AS base 

WORKDIR /app 
EXPOSE 80 
FROM mcr.microsoft.com/dotnet/framework/runtime:4.8-windowsservercore-ltsc2019 AS build 

WORKDIR /src 
COPY ["SimpleFrameworkApp.csproj", "SimpleFrameworkApp/"] 
RUN dotnet restore "SimpleFrameworkApp.csproj" 
COPY . . 
WORKDIR "/src/SimpleFrameworkApp" 
RUN dotnet build "SimpleFrameworkApp.csproj" -c Release -o /app/build   

FROM build AS publish 
RUN dotnet publish "SimpleFrameworkApp.csproj" -c Release -o /app/publish /p:UseAppHost=false  

FROM base AS final 

WORKDIR /app 

COPY --from=publish /app/publish . 

ENTRYPOINT ["dotnet", "SimpleFrameworkApp.dll"] 